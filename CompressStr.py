def compress(arr):

    count = {}
    st = ''

    for letter in arr:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    print(count)

    for i,j in count.items():
        st = st + str(i) + str(j)
    print(st)

if __name__ == '__main__':
    compress('AABBccDDaaEEEFFff')