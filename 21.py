a = "정수"
b = "태희"
c = "환준"
d = "세영"
a1 = 20
a2 = 19

# def caht(name1, name2): 
   # print("%s: 안녕? 넌 몇 살이니?" % name1)
   # print("%s: 나? 나는 20살이야!" % name2)
    
   # chat(a, b)
   # chat(c, d)
    
def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age) + "살이야!")
    
chat("a", "b", a1)
chat("c", "d", a2)
    