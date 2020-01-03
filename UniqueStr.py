def unique(arr):

    i = 0
    count = 0
    l = len(arr)
    while i != l-1:
        if arr[i] == arr[i+1]:
            count += 1
            break
        else:
            count = 0
        i += 1

    if count == 0:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    unique('abcde')