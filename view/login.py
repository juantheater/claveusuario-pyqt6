from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont, QPalette, QColor
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scale=70
        self.setStyleSheet("background-color: #2c3e50;") # Dark blue-gray hex

        # Central widgets
        self.central_widget=QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Widgets de entradas al formulario
        self.form=QWidget()
        #self.setStyleSheet("border:1px solid red;")
        self.form_input=QWidget()
        self.form_input.setMaximumHeight(300)

        # Configuracion de titulos del formulario
        self.title=QLabel("Login")
        self.title.setStyleSheet("color: white;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.font=QFont("Arial",25)
        self.font.setBold(True)
        self.title.setFont(self.font)
        self.title.setMaximumHeight(50)

        # Configuraciones de entrada de datos
        # Correo -----------------------------------
        email=QLineEdit()
        email.setPlaceholderText("Email")
        email.setTextMargins(22,0,0,0)
        email.setMinimumSize(int(self.form.width()*0.6),50)
        email.setStyleSheet('border-radius:15px;background-color:#19293B;font-size:14px;font-weight:bold')

        # Clave de acceso --------------------------
        password=QLineEdit()
        password.setPlaceholderText("Contraseña")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setTextMargins(22,0,0,0)
        password.setMinimumSize(int(self.form.width()*0.6),50)
        password.setStyleSheet('border-radius:15px;background-color:#19293B;font-size:14px;font-weight:bold')

        # Boton de enviar ---------------------------
        login_btn=QPushButton()
        login_btn.setText("Submit")
        login_btn.setMinimumSize(int(self.form.width()*0.6),50)
        login_btn.setStyleSheet('border-radius:15px;background-color:#5591D9;font-size:14px;font-weight:bold')
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Disenos
        self.general_layout=QHBoxLayout()
        self.form_layout=QVBoxLayout()
        self.form_imput_layout=QVBoxLayout()
        
        # Configurar imagen
        img=QLabel()
        pixmap=QPixmap("/Users/Juan/Documents/claveusuario-pyqt6/img/login.jfif").scaled(450,650)
        img.setPixmap(pixmap)

        # Configuracion de los disenos
        # Entradas
        self.form_imput_layout.addWidget(email)
        self.form_imput_layout.addWidget(password)
        self.form_imput_layout.addWidget(login_btn)
        self.form_imput_layout.setSpacing(10)

        self.form_input.setLayout(self.form_imput_layout)

        # Form
        self.form_layout.addWidget(self.title)
        self.form_layout.addWidget(self.form_input)
        
        self.form.setLayout(self.form_layout)
        
        # Diseño general
        self.general_layout.addWidget(img)
        self.general_layout.addWidget(self.form)
        self.general_layout.setContentsMargins(0,0,0,0)

        self.central_widget.setLayout(self.general_layout)

        # Configurar tamaño maximo y minimo de la ventana
        self.setMinimumSize(16*self.scale,9*self.scale)
        self.setMaximumSize(16*self.scale,9*self.scale)

        # Mostrar
        self.show()