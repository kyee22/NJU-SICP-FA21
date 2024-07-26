

def multiplier():
    print('iter is going on...')
    return 2

lst = [1,2,3]

lt = [x * multiplier() for x in lst]
it = (x * multiplier() for x in lst)

print('....')
print(next(it))
print('.....')
print(next(it))