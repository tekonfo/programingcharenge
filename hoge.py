def solution(M, N):
    if M == N:
        return 0

    # このままだとO(N)なので最悪10^9
    answer = M
    for i in range(M+1, N+1):
        answer = answer ^ i

    return answer

print(solution(11, 16))
