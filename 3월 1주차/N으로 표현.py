def solution(N, number):
    if N == number:
        return 1
        
    s = [ set() for x in range(8) ] 

    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )

    for i in range(1, 8):
        for j in range(i):
            for rs1 in s[j]:
                for rs2 in s[i-j-1]:
                    s[i].add(rs1 + rs2)
                    s[i].add(rs1 - rs2)
                    s[i].add(rs1 * rs2)
                    if rs2 != 0:
                        s[i].add(rs1 // rs2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer