def missing(arr,arr_test):
    count = {}

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count,'After first loop')

    for i in arr_test:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1
    print(count,'After second loop')

    for k, l in count.items():
        if l == 1:
            print('missing element is: ',k)

if __name__ == '__main__':
    missing([1,2,3,4,5,6,],[3,7,2,1,4,6,7])