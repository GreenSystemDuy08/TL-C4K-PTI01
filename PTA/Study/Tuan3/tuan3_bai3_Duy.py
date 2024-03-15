class Xe:
    def __init__(self, LoaiXe, HangXe, MauSac, SoChoNgoi, SoBanhXe, GiaTien):
        self.LoaiXe = LoaiXe
        self.HangXe = HangXe
        self.MauSac = MauSac
        self.SoChoNgoi = SoChoNgoi
        self.SoBanhXe = SoBanhXe
        self.GiaTien = GiaTien
    
    def InThongTin(self):
        print("Loại xe:",self.LoaiXe)
        print("Hãng xe:",self.HangXe)
        print("Màu của xe:",self.MauSac)
        print("Số chỗ ngồi:",self.SoChoNgoi)
        print("Số bánh xe:",self.SoBanhXe)
        print("Giá tiền:",self.GiaTien)
    
#Khai Báo đối tượng 
Ford = Xe('Xe Bán Tải','Ford','Xám',8,8,'1 triệu')