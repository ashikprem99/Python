def remove_newlines(fname):
    f = open(fname).readlines()
    return [s.rstrip('\n') for s in f]
print(remove_newlines("test.txt"))
