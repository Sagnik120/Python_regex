#finding the word of maximum length

a = input()  #sachin rameshhhh virat 
a = a.split()  #a=[s,r,v]

maxx = a[0]

max_len = len(a[0])

for i in a:
  if len(i)>max_len:
    max_len = len(i)
    maxx = i
print(maxx)

