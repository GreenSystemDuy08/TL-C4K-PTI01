class ChuNhat():
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def caculator(self):
        # print("Dai = 10", self.dai)
        # print("Rong = 5", self.rong)
        P = (self.dai + self.rong)*2
        return P
        
    
Hinhchunhat = ChuNhat(5,10)
print(Hinhchunhat.caculator())