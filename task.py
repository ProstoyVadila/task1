

def task(numbers: str) -> int:
    arr = [int(i) for i in numbers]
    left = 0
    right = len(arr) - 1
    mid = len(arr) // 2

    while left <= right:
        if arr[mid] != 0:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return mid + 1


if __name__ == '__main__':
    print(task('111111111111111111111111100000000'))
