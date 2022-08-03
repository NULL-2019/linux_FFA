a = 'aff.sd.al.aaa.bb_CC_DD_OK<'

b = a.split('.')[1]
c = a.split('_')[-1]
d = a.split('_')[0]
E = a.split(".")
print(E)#分割完之后会生成一个列表，然后就可以通过索引的方式来进行访问

print(b)
print(c)
print(d)