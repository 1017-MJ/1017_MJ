x = 3
y = 1
z = 0

if x > 2:
    print("hello", "\n")
    
if x < y :
    print("x보다 y가 크다")
print("y가 x보다 크지 않기 (false) 때문에 출력 안된다.", "\n")

if not x < y:
    print("x보다 y가 크지 않다", "\n")
print("not이 붙어서 ture이기 때문에 출력된다", "\n")

if z > y and x > y: 
    print("z가 y보다 크다(false), x가 y보다 크다(true)")
print("두 가지 중 하나만 맞으면(true) 출력된다", "\n")