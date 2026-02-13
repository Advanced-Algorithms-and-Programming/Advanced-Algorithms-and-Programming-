//Approach A

def LinearSpace(A, k):
    n = len(A)
    if n == 0:
        return
    effective_k = k % n
    Buffer = [0] * n
    
    for i in range(n):
        new_position = (i + effective_k) % n
        Buffer[new_position] = A[i]
        
    for i in range(n):
        A[i] = Buffer[i]

//Approach B
def StepByStepShift(A, k):
    n = len(A)
    if n == 0:
        return
    effective_k = k % n
    
    for step in range(effective_k):
        temp = A[n - 1]
        for index in range(n - 1, 0, -1):
            A[index] = A[index - 1]
        A[0] = temp
