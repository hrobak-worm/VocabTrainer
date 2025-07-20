import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from views.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbAddWord.clicked.connect(lambda: print("Додати слово…"))
        self.ui.pbLearn.clicked.connect(lambda: print("Вчити слова…"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())