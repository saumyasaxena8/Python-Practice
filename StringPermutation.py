def permute(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i,let in enumerate(s):
            print('i:',i)
            print('let',let)
            for perm in permute(s[:i] + s[i+1:]):
                print('perm is:',perm)
                out += [let+perm]
                print(out)
    return out
