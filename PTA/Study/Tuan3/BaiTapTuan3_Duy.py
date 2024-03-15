class Cho:
    def __init__(self, Ten, Giong, Tuoi, MauSac, CanNang, MauLong):
        self.Ten = Ten
        self.Giong = Giong
        self.Tuoi = Tuoi
        self.MauSac = MauSac
        self.CanNang = CanNang
        self.MauLong = MauLong

    def InThongTin(self):
        print("Tên của chú chó:",Husky.Ten)
        print("Giống của",Husky.Ten,"là:",Husky.Giong)
        print("Tuổi của",Husky.Ten,":",Husky.Tuoi)
        print("Chú chó",Husky.Ten,"có màu",Husky.MauSac)
        print("Cuối cùng,",Husky.Ten,"có cân nặng là",Husky.CanNang)

    def ThayDoiMauSac(self):
        new_color = input("Nhập màu mới cho chóa: ")
        self.MauSac = new_color
Husky = Cho("Husky","Husky","3","Xám","15kg","Xám")
Husky.ThayDoiMauSac()
Husky.InThongTin()