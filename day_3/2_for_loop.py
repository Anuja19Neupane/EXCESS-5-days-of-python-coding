species=['dog','pig','mango']
for i in species: # list ko lagi yo for loop use hunxa
    print(i)


# range(start,stop,step)
for a in range(0,10): # range(start,stop) 
    print(a)
# range(0,11):0,1,2,3,4,5,6,7,8,9
print("next")
for b in range(0,10,5): # output: 0,5
    print(b)
print("next")
for c in range(1,10):
    if c==3: # c 2 hunjel samma ko matra limit thyo,c 3 vayo,limit cross breakup 
        break
    print(c)
print("next")
for d in range(5): # range(start) , index 5 samma ho range
    print(d)
