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
                else:
                    rs = False
                    break
            else:
                rs = False
                break
        answer.append(rs)
        
    return answer

program, flag_rules, commands = "line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]
solution(program, flag_rules, commands)