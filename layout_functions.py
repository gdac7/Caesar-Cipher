from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QSpinBox, QPushButton
from PyQt5.QtCore import Qt
from custom_widgets import AppHeading
from jsonfile_functions import save_encrypt_txt, copy_encrypt_text


def setInitialLayout(w):
        layout = QVBoxLayout()
        widgets = (
            AppHeading("Caesar Cipher Encryptor-Decryptor", 20, alignment=Qt.AlignCenter, color='yellow'),
            QPushButton('encrypt/decrypt an sentence'),
        )

        widgets[1].clicked.connect(w.show_encrypt_page)

        for item in widgets:
            layout.addWidget(item)
        return layout

def setEncryptPageLayout(w):
    layout = QVBoxLayout()
    widgets = (
        AppHeading('Write your sentence', 15, color="yellow", alignment=Qt.AlignCenter),
        QLineEdit(),
        AppHeading('Choose the shift number', 15, color="yellow", alignment=Qt.AlignCenter),
        QSpinBox(),
        QPushButton('encrypt!'),
        QPushButton('decrypt!'),
    )

    widgets[1].setPlaceholderText('maximum 100 characters')
    widgets[1].setFixedHeight(30)
    widgets[1].setMaxLength(100)

    widgets[3].setMinimum(1)
    widgets[3].setFixedHeight(30)

    widgets[4].clicked.connect(lambda encrypt_with_text: w.encrypt_and_decrypt(widgets[1].text(), widgets[3].value(), 0))
    widgets[5].clicked.connect(lambda decrypt_with_text: w.encrypt_and_decrypt(widgets[1].text(), widgets[3].value(), 1))

    for item in widgets:
        layout.addWidget(item)
    return layout

def postEncryptPageLayout(shifted_text, shift_value, w):
    layout = QVBoxLayout()
    widgets = (
        AppHeading('Your encrypted sentence:', 15, color="yellow"),
        AppHeading(shifted_text, 25, "red"),
        QPushButton('Save in .json file'), 
        QPushButton('Copy'), 
        QPushButton('Return to initial page'), 
        )

    widgets[1].setWordWrap(True)
    widgets[2].clicked.connect(lambda save_text: save_encrypt_txt(shifted_text, shift_value, widgets[2]))
    widgets[3].clicked.connect(lambda copy_text: copy_encrypt_text(shifted_text, widgets[3]))
    widgets[4].clicked.connect(w.return_to_initial_page)
    
    for item in widgets:
        layout.addWidget(item)
    return layout