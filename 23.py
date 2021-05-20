def sayhello(name, age):
    if age < 10:
        print("안녕, " + name)
    elif age <=20 and age >= 10:
        print("안녕하세요, " + name)
    else:
        print("안녕하십니까, " + name)

sayhello("태희", 20)
sayhello("정수", 6)
sayhello("세영", 40)
sayhello("철수", 10)