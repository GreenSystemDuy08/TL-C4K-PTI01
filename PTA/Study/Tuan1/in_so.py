n = int(input("Hãy nhập số kết thúc vào đây: "))
def tinh_so(n):
    n1 = []
    for i in range(1,n):
        if i % 2 == 0:
            n1.append(i)
    print(n1)
tinh_so(n)