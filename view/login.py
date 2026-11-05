from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scale=70

        # Configurar tamaño maximo y minimo de la ventana
        self.setMinimumSize(16*self.scale,9*self.scale)
        self.setMaximumSize(16*self.scale,9*self.scale)

        # Mostrar
        self.show()