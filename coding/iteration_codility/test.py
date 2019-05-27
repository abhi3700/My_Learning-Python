num = "{0:b}".format(45)
# print(len(num))
print(num)
count = 0
var = []
i = 0
for x in map(int, num):
    # print(x)

    var[i] = x
    if (x == 1):
        count+=1
    i+=1
print(count)
print(var)