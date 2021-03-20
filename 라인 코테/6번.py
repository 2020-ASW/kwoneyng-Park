from collections import deque
def solution(program, flag_rules, commands):
    answer = []
    
    flags = {}
    
    for flag_rule in flag_rules:
        flag_name, flag_argument_type = flag_rule.split()
        if not flags.get(flag_name):
            flags[flag_name] = flag_argument_type
            
    
    for command in commands:
        command = deque(command.split())
        program_name = command.popleft()
        if program_name != program:
            answer.append(False)
            continue
        flag_name = ''
        rs = True
        while command:
            argument = command.popleft()
            # flag 이름이 나오기 전이면 flag 이름을 받아옴, type이 Null인 경우는 다음 flag를 찾아야함
            if not flag_name and flags.get(argument):
                if flags[argument] != 'NULL':
                    flag_name = argument
            # flag 이름을 받은 경우에는 type 체크를 진행함
            # string인 경우에는 알파벳 대소문자로만 이루어져있고 number일 경우 숫자로만 이루어져 있음
            elif flag_name:
                if flags[flag_name] == 'STRING' and argument.isalpha():
                    flag_name = ''
                elif flags[flag_name] == 'NUMBER' and argument.isdigit():
                    flag_name = ''
                # string들을 받기 시작합니다. 하나 이상 string이 있어야합니다.ㅌ
                elif flags[flag_name] == 'STRINGS' and argument.isalpha():
                    # 다음 argument가 string일 경우 계속 받아줍니다.
                    while command and command[0].isalpha():
                        command.popleft()
                    flag_name = ''
                elif flags[flag_name] == 'NUMBERS' and argument.isdigit():
                    while command and command[0].isdigit():
                        command.popleft()
                    flag_name = ''
                else:
                    rs = False
                    break
            # flag 이름을 받지 않았는데 flag_name이 아닌것을 받을 경우 False
            else:
                rs = False
                break
        answer.append(rs)
        
    return answer