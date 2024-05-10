import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import json

class DialogPage(QDialog):
    class HomeworkList:
            def __init__(self):
                self.items = []

            def add_item(self, item):
                self.items.append(item)

            def all_completed(self):
                completed = True
                for item in self.items:
                    if item.completed == False:
                        completed = False
                        print(item.name)
                    if completed:
                        print("All Finished!")
    def add_item(self, HomeworkList):
        hw_list = HomeworkList()
        hw_list.add_item(Homework("Lập trình App Producer" , 3))
        hw_list.add_item(Homework("Làm văn", 2, True))
        hw_list.add_item(Homework("Lập trình GameMaker", 3))
        hw_list = HomeworkList.hw_list()
        items = QListWidgetItem(hw_list)
        self.page_listwidget.listWidget.addItem(items)
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/dialog.ui", self)
        self.bt_export.clicked.connect(self.Export)
    def Export(self):
        class Homework:
            def __init__(self, name, priority, completed = False):
                self.name = name
                self.priority = priority
                self.completed = completed


        class HomeworkList:
            def __init__(self):
                self.items = []

            def add_item(self, item):
                self.items.append(item)

            def all_completed(self):
                completed = True
                for item in self.items:
                    if item.completed == False:
                        completed = False
                        print(item.name)
                    if completed:
                        print("All Finished!")

        hw_list = HomeworkList()
        hw_list.add_item(Homework("Lập trình App Producer" , 3))
        hw_list.add_item(Homework("Làm văn", 2, True))
        hw_list.add_item(Homework("Lập trình GameMaker", 3))
    def add_item(self, HomeworkList):
        hw_list = HomeworkList.hw_list()
        items = QListWidgetItem(hw_list)
        self.page_listwidget.listWidget.addItem(items)
    def set_page(self, page_listwidget):
        self.page_listwidget = page_listwidget

    def load_json_data():
        HomeworkList = list()
        with open("new_data.json", "r") as json_in:
            json_data = json.load(json_in)
        HomeworkList.extend(json_data)
        return HomeworkList

    def write_json_data(json_data):
        with open("new_data.json", "w") as json_out:
            json.dump(json_data, json_out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = DialogPage()
    Dialog.show()
    app.exec()