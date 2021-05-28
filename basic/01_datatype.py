#  *************
# ---Data Type ---
#  *************

'''
Python has Five standard types
scalar
    Number : int, floot, complex
    String : str
vector : List, Tuple, Dictionary, Set
'''
'''
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])

Python List
'''
ls = ['adbd',786, 2.23,'john,70.2'] #atomic level
tinylist = [123, 'john']

# Create : ls 에 '100'을 추가 Create
ls.append('100')

# Read : ls 의 목록을 출력
print(ls)

# Update : ls와 tinyls 의 결합
newlist = ls + tinylist

# Delete : ls 에서 786을 제거
ls.remove(786)

#-------------------------------------------------------------------

# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
ls.append('100')
# Read: ls 의 목록을 출력
print(ls)
# Update: ls와 tinyls 의 결합
newls = ls + tinyls
# Delete: ls 에서 786을 제거
ls.remove(786)

#--------------------------------------------------------------------

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
tp2 = ('100')
tp = tp + tp2
# Read: tp 의 목록을 출력
print(tp)
# Update: tp와 tinytp 의 결합
newtp = tp + tinytp

# Delete: tp 에서 786을 제거

tp = ('abcd', 2.23, 'john', 70.2)

# ------------------------------------------------------------------

# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍', '30세'}
# Create: dt 에 '100'을 추가 Create
dt['tom'] = 100
# Read: dt 의 목록을 출력
print(dt)
# Update: dt와 tinydt 의 결합
dt.update(tinydt)
# Delete: dt 에서 'abcd' 제거
del dt[0]
