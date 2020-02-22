def multiply(arr, n):
    if n<=1:
        return

    prev = arr[0]
    arr[0]  = arr[0] * arr[1]

    for i in range(1, n-1):
        curr = arr[i]
        arr[i] = prev * arr[i+1]
        prev = curr
    arr[n-1] = prev * arr[n-1]

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = len(arr)
    multiply(arr, n)
    print(arr)