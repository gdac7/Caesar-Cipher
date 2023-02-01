from PyQt5.QtWidgets import QLabel

class AppHeading(QLabel):
    def __init__(self, text, size=None, color=None, alignment=None):
        super().__init__()
        self.setText(text)
        if size:
            font = self.font()
            font.setPointSize(size)
            self.setFont(font)
        if color:
            self.setStyleSheet(f"color: {color};")
        if alignment:
            self.setAlignment(alignment)

