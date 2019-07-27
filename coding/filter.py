"""
    __Definition__: `Filter` is to select items with a pattern - 'abc', etc.
    __Description__: 2 methods are described here.
"""
lst = ['a', 'ab', 'abc', 'bac']

# M-1
res = [k for k in lst if 'ab' in k]
print(res)  # ['ab', 'abc']

# M-2
res2 = filter(lambda k: 'ab' in k, lst)
# for i in res:
#     print(i)  # ['ab', 'abc']
print(res2)