# Q-1 : He provides me this dictionary and he want only keys having valuei.e skipping the "None"

d = {'a':1,'b':None,'c':"ABC",'d':"123"}
# output: a, c, d
Output = [key for key, value in d.items() if value is not None]
print(Output)





