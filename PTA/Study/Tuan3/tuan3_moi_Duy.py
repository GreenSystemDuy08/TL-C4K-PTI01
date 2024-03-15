class Xe:
    def __init__(self, hang, mausac, giatien):
        self.hang = hang
        self.mausac = mausac
        self.giatien = giatien
    
    def KhoiDong(self):
        print(f"Xe {self.hang} đang khởi động")
        
class XeHoi(Xe):
    def ChayBangBonBanh(self):
        print(f"Xe {self.hang}, {self.mausac}, {self.giatien}$ đang chạy về phía trước bằng động cơ")
        
class XeDap(Xe):
    def DapBangHaiChan(self):
        print(f"Xe {self.hang}, {self.mausac}, {self.giatien}$ đang được đạp về phía trước")


# Tạo đối tượng xe hơi từ lớp con XeHoi
xe_hoi = XeHoi("Toyota", "Trắng", 500000000)
xe_hoi.KhoiDong()
xe_hoi.ChayBangBonBanh()

# Tạo đối tượng xe đạp từ lớp con XeDap
xe_dap = XeDap("Forever", "Đen", 3000000)
xe_dap.KhoiDong()
xe_dap.DapBangHaiChan()