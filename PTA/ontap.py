a = int(input("Nhập chiều cao bạn A: "))
b = int(input("Nhập chiều cao bạn B: "))
c = int(input("Nhập chiều cao bạn C: "))
if a == b and b == c and c == a:
    print("Ba bạn đều cao không khác gì nhau!!!")
elif a > b and a > c:
    print("Bạn cao nhất là bạn cao mét:", a)
elif a < 0 or b < 0 or c < 0:
    print(":(")
    print("YOUR APPLICATION RAN IN A PLOBLEM AND NEED TO RELAUNCH!!!")
    print("CODE: Chiều cao một bạn nào đó không hợp lệ!!!")
elif b > c and b > a:
    print("Bạn cao nhất là bạn cao mét:", b)
else:
    print("Bạn cao nhất là bạn cao mét:", c)