def func1(N, colors):
    posit_dict = dict()
    for j, char in enumerate(colors):
        if char not in posit_dict:
            posit_dict[char] = j + 1
        else:
            posit_dict[char] = -1
    counter = 0
    positions = []
    for k, v in posit_dict.items():
        if v != -1:
            counter += 1
            positions.append(v)
    print(counter)
    print(' '.join(map(str, positions)))


# colors = '7' \
#          'AABCDCE' \
#          '12' \
#          'AABBCCDEFDFE' \
#          '8' \
#          'HEYSHYSH'
# N = 3
# func1(N, colors)

def func2(N, A):
    def max_subarrays(arr):
        n = len(arr)
        zeros = [i for i in range(n) if arr[i] == 0]
        if not zeros:
            return n * (n + 1) // 2
        total_count = 0
        for i in range(len(zeros)):
            left = zeros[i - 1] + 1 if i > 0 else 0
            right = zeros[i]
            count = (right - left + 1) * (left - zeros[i - 2] if i > 1 else left + 1) if i > 0 else (right + 1) * (
                        n - right)
            total_count += count
        return total_count
    result = max_subarrays(A)
    for i in range(len(A)):
        if A[i] == 1:
            A[i] = 0
            result = max(result, max_subarrays(A))
            A[i] = 1
    print(result)


A = [1, 0, 0, 1, 1]
N = 5


def subArrayCount(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += len(arr) - i
            continue
        else:
            flag = False
            for j in range(i, len(arr)):
                if arr[j] == 0:
                    flag = True
                if flag:
                    count += 1
    return count

# def solve(N, A):
#     result = 0
#     for i in range(N):
#         if A[i] == 1:
#             A[i] = 0
#             result = max(result, subArrayCount(A))
#             A[i] = 1
#     print(result)

# def solve(N, A):
#     count = 0
#     zeros = [i for i in range(N) if A[i] == 0]
#     if len(zeros) == 0:
#         count = N*(N+1)//2
#     else:
#         count = (zeros[0]+1)*(N-zeros[-1])
#         for i in range(1,len(zeros)):
#             count += (zeros[i]-zeros[i-1])*(zeros[i-1]+1)
#     print(count)

A = [1, 0, 0, 1, 1]
N = 5

solve(N, A)
