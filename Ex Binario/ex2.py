A = [1,2,3,4,5]

def solution(A : list, K):
    if len(A) == 0:
        return A
    for a in range(0, K):
        comeco = A.pop()
        A.insert(0,comeco)
        print(A)
    return A

solution(A, 5)