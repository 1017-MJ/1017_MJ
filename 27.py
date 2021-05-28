x = [3,2,4,1]

for n in x:           
    print(n)        
    

x = [3,2,4,1]
y = ["Hello", "There"]
for c in y:           
    print(c)        


x = [3,2,4,1]
    #0,1,2,3
y = ["Hello", "There"]

print(x.index(4))        
print(y.index("Hello"))  



x = [3,2,4,1]
    #0,1,2,3
y = ["Hello", "There"]

print("bye" in y)    
print("Hello" in y)  

if "Hello" in y:
    print("Hello가 있어요.")
    
if "bye" in y:
    print("bye")
print("bye는 없어요.")