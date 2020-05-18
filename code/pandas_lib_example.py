import pandas as pd


data = ['a','b','c','d']
s = pd.Series(data)
print(s)

data = ['a','b','c','d']
s = pd.Series(data,index=[10, 20, 30, 40])
print(s)


data = [['Alex',10],['Mark',12],['Santa',15]]
frame = pd.DataFrame(data,columns=['Name','Age'])
print(frame)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
frame = pd.DataFrame(data,columns=['Name','Age'])
print(frame)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
frame = pd.DataFrame(data)
print(frame)

#f = pd.Panel(frame)

data = {'Item1' : pd.DataFrame(data), 
        'Item2' : pd.DataFrame(data)}
p = pd.Panel(data)
print(p)
