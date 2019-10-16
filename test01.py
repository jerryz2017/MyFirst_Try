print('第一题')
a = int(input('请输入第一个数字a:'))
b = int(input('请输入第一个数字b:'))
c = int(input('请输入第一个数字c:'))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)
