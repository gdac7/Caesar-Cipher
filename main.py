from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import string
import sys
from caesar_cipher import caesar 
from layout_functions import setInitialLayout, setEncryptPageLayout, postEncryptPageLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caesar's cipher")
        self.setFixedSize(600, 400)
        self.last_coded_text = ""
        self.initial_page = QWidget()
        self.initial_page.setLayout(setInitialLayout(self))
        self.setCentralWidget(self.initial_page)


    def show_encrypt_page(self):
        encrypt_layout = QWidget()
        encrypt_layout.setLayout(setEncryptPageLayout(self))   
        self.setCentralWidget(encrypt_layout)


    def encrypt_and_decrypt(self, text=None, shift=None, code=0):
        if code == 0:
            self.last_coded_text = caesar(text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation], code)
        else:
            self.last_coded_text = caesar(text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation], code)
        self.show_result(self.last_coded_text, shift)

        
    def show_result(self, text, shift):
        widget = QWidget()
        widget.setLayout(postEncryptPageLayout(text, shift,  self))
        self.setCentralWidget(widget)
        

    def return_to_initial_page(self):
        widget = QWidget()
        widget.setLayout(setInitialLayout(self))
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("styles/styles.qss", encoding="utf-8") as file:
            styles = file.read()
    app.setStyleSheet(styles)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())