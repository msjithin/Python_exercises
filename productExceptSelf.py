def product_except_self(arr):

    # Replace this placeholder return statement with your code
    n = len(arr)
    res = [1] * n
    left = 0
    right = n-1

    left_pd = 1
    right_pd = 1

    while left < n and right > -1:
        res[left] *= left_pd 
        res[right] *= right_pd

        left_pd *= arr[left]
        right_pd *= arr[right]

        left += 1
        right -= 1

    return res 


    # n = len(arr)
    # res = [1] * n
    # forward = [1] * n
    # backward = [1] * n

    # for i in range(1, n):
    #     forward[i] = forward[i-1] * arr[i-1]

    # for i in range(n-2, -1, -1):
    #     backward[i] = backward[i+1] * arr[i+1]

    # for i in range(n):
    #     res[i] = forward[i] * backward[i]

    # return res


# Driver code
def main():
    
    inputList = [[1, 5, 10], [3, 5, 0, -3, 1], [7, 8, 9, 10, 11], [2, -4, -8, -11, 11], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5]]
    
    # For each input, print the input and its maximum depth
    for i in range(len(inputList)):
        print (str(i + 1) + '.\tnums:', inputList[i])
        print ('\tres:', product_except_self(inputList[i]))
        print ('-' * 100)

if __name__ == '__main__':
    main()
