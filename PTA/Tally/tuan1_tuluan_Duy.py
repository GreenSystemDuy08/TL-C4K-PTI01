dulieu = input("Nhập thời gian theo định dạng 'hh:mm:ss':")
danhsach1 = dulieu.split(":")
def KiemTraThoiGianDaNhap():
    for i in danhsach1:
        if 0 <= int(danhsach1[0]) <= 23:
            print("Hello!")
        if 0 <= int(danhsach1[1]) <= 59:
            print("Hello 1")
        if 0 <= int(danhsach1[2]) <= 59:
            print("Bye!")
KiemTraThoiGianDaNhap()