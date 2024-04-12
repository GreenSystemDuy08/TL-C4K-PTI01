class Homework:
    def __init__(self, name, priority, completed = False):
        self.name = name
        self.priority = priority
        self.completed = completed
    def duyet_phan_tu():
        for Homework in Homeworks:
            print("Tên bài tập: ", Homework.name,", Trạng thái: " ,Homework.completed)
            print("--------------------------------------------------")
    def all_finished():
        for Homework in Homeworks:
            if Homework.completed == "Chưa hoàn thành":
                print("Bài tập chưa hoàn thành:", Homework.name)

Homework1 = Homework("Lập trình App Producer", "Cao", "Chưa hoàn thành")
Homework2 = Homework("Làm văn", "Trung bình", "Đã hoàn thành")
Homework3 = Homework("Lập trình GameMaker", "Thấp", "Chưa hoàn thành")
Homeworks = [Homework1, Homework2, Homework3]
Homework4 = Homework("Làm toán", "Trung Bình", "Đã hoàn thành")
Homeworks.append(Homework4)

Homework.duyet_phan_tu()
Homework.all_finished()
class HomeworkList:
    def __init__(self):
        self.items = [Homework1, Homework2, Homework3]

    def add_item(self, item):
        self.items.append(item)