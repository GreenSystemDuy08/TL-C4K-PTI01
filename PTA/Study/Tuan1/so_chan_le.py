a = int(input("Nhập số vào đây đê bạn ê: "))
def so_chan_le(a):
    if a == 0:
        print("Số 0 không là số chẵn và lẻ!")
    elif a < 0:
        print("Đây là số âm, không phải số dương!!!")
    elif a % 2 == 0:
        print("Đây là số chẵn!")
    else:
        print("Đây là số lẻ!")
so_chan_le(a)