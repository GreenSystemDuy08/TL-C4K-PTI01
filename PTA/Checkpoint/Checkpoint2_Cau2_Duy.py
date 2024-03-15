class HocSinh:
    def __init__(self,Ten,DiaChi,ChieuCao,CanNang):
        self.Ten = Ten
        self.DiaChi = DiaChi
        self.ChieuCao = ChieuCao
        self.CanNang = CanNang
    def ThongTinHocSinh(self):
        self.Ten = "Duy"
        self.DiaChi = "123 Tên Lửa"
        self.ChieuCao = "1m80"
        self.CanNang = "60kg"
    ThongTinHocSinh('self')
HocSinh1 = HocSinh("Duy","123 Tên Lửa","1m80","60kg")