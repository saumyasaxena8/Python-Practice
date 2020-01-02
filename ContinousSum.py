def continousSum(arr):

    # add = 0
    # val = 0
    #
    # for i in arr:
    #     add += i
    #     if val < add:
    #         val = add
    # print(val,'add')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        print(current_sum,'current')
        max_sum = max(current_sum, max_sum)
        print(max_sum,'max')


if __name__ == '__main__':
    continousSum([1,2,-1,3,4,10,10,-10,-1])