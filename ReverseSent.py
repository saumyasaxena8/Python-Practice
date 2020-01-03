# Using pythons in-built functions
#
# def rev_word(s):
#     print(" ".join(reversed(s.split())))
#
# def rev_words2(s):
#     print(" ".join(s.split()[::-1]))

def rev_words3(s):

    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
            print(words)

        i += 1

    print(' '.join(reversed(words)))

if __name__ == '__main__':
    rev_words3('This is a sentence  ')
