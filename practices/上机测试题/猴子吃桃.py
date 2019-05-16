rest = 1


def res_before(r):
    return (r+1)*2


for n in range(9):
    rest = res_before(rest)
print(rest)
