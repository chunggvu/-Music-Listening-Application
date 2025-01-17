from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import MySQLdb as mdb
import re

class Ui_SignupWindow(object):
    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()
            
    def goToLogin(self):
        try:
            from loginScreen import Ui_LoginWindow
            self.login_window = QtWidgets.QMainWindow()
            self.ui = Ui_LoginWindow()
            self.ui.setupUi(self.login_window)
            self.login_window.show()
            self.closeWindows()
        except ImportError:
            pass

    def signup(self):
        role = 0
        premium = 0
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        retype_password = self.password_again.text()
        
        db = mdb.connect('localhost','root','','music_app')
        usernameDb = db.cursor()
        emailDb = db.cursor()
        usernameDb.execute("SELECT * FROM `user_management` WHERE username = '"+username+"'")
        emailDb.execute("SELECT * FROM `user_management` WHERE email = '"+email+"'")
        username_check = usernameDb.fetchone()
        email_check = emailDb.fetchone()

        if username_check:
            QMessageBox.critical(None, "Register fail!", "This username has been selected!")
        elif email_check:
            QMessageBox.critical(None, "Register fail!", "This email has been used!")
        elif len(username) == 0:
            QMessageBox.critical(None, "Register fail!", "Username is required!")
        elif len(email) == 0:
            QMessageBox.critical(None, "Register fail!", "Email is required!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.critical(None, "Register fail!", "Your email address is invalid!")
        elif len(password) == 0:
            QMessageBox.critical(None, "Register fail!", "Password is required!")
        elif len(password) > 16 or len(password) < 8:
            QMessageBox.critical(None, "Register fail!", "Password must be more than 8 characters less than 16 characters!")
        elif password != retype_password:
            QMessageBox.critical(None, "Register fail!", "Passwords do not match!")
        else:
            query = db.cursor()
            query.execute("INSERT INTO `user_management` (`username`, `email`, `password`, `premium`, `role`) VALUES ('"+username+"', '"+email+"', '"+password+"', '"+str(premium)+"', '"+str(role)+"')")
            db.commit()
            QMessageBox.information(None, "Register success!", "Please login to continue!")
            self.goToLogin()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 920)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color:white;\n"
"font-family:\"Arial Rounded MT Bold\"\n"
"}\n"
"\n"
"#background {\n"
"background-color:black;\n"
"}\n"
"\n"
"#signup_form {\n"
"background-color:#121212;\n"
"border-radius: 15px\n"
"}\n"
"\n"
"#signup_form QLineEdit {\n"
"background-color:#121212;\n"
"border-radius: 4px;\n"
"border: 1px solid gray;\n"
"padding: 0px 10px;\n"
"height: 55px;\n"
"color:white;\n"
"}\n"
"\n"
"#signup_form QLineEdit:hover {\n"
"border: 1.5px solid white\n"
"}\n"
"\n"
"#signup_form QLineEdit:focus {\n"
"border: 1.5px solid white\n"
"}\n"
"\n"
"#forgotPsw {\n"
"border:none;\n"
"background-color:#121212\n"
"}\n"
"\n"
"#signupBtn {\n"
"background-color:#1BD760;\n"
"border-radius:5px;\n"
"color:white;\n"
"padding:5px;\n"
"height:40px\n"
"}\n"
"\n"
"#loginBtn {\n"
"background-color:#121212;\n"
"border:none;\n"
"color:white\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout_2.setContentsMargins(400, 150, 400, 200)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.signup_form = QtWidgets.QWidget(self.background)
        self.signup_form.setObjectName("signup_form")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.signup_form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.signup_title_field = QtWidgets.QWidget(self.signup_form)
        self.signup_title_field.setObjectName("signup_title_field")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.signup_title_field)
        self.verticalLayout_4.setContentsMargins(100, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.signup_title_field)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.signup_title_field)
        self.in4_blank_field = QtWidgets.QWidget(self.signup_form)
        self.in4_blank_field.setObjectName("in4_blank_field")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.in4_blank_field)
        self.verticalLayout_5.setContentsMargins(100, 0, 100, 0)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.username = QtWidgets.QLineEdit(self.in4_blank_field)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.verticalLayout_5.addWidget(self.username)
        self.email = QtWidgets.QLineEdit(self.in4_blank_field)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.verticalLayout_5.addWidget(self.email)
        self.password = QtWidgets.QLineEdit(self.in4_blank_field)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.verticalLayout_5.addWidget(self.password)
        self.password_again = QtWidgets.QLineEdit(self.in4_blank_field)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.password_again.setFont(font)
        self.password_again.setObjectName("password_again")
        self.verticalLayout_5.addWidget(self.password_again)
        self.verticalLayout_3.addWidget(self.in4_blank_field)
        self.signup_button_field = QtWidgets.QWidget(self.signup_form)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.signup_button_field.setFont(font)
        self.signup_button_field.setObjectName("signup_button_field")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.signup_button_field)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.signup_button_field)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(190, 0, 190, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.signupBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.signupBtn.setFont(font)
        self.signupBtn.setObjectName("signupBtn")
        self.verticalLayout_7.addWidget(self.signupBtn)
        self.verticalLayout_6.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.signup_button_field)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setContentsMargins(150, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.loginBtn = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        font.setUnderline(True)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.verticalLayout_3.addWidget(self.signup_button_field)
        self.verticalLayout_2.addWidget(self.signup_form)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create account"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.password_again.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signupBtn.setText(_translate("MainWindow", "Sign up"))
        self.label_2.setText(_translate("MainWindow", "Already a member?"))
        self.loginBtn.setText(_translate("MainWindow", "Log in"))

        self.signupBtn.clicked.connect(self.signup)
        self.loginBtn.clicked.connect(self.goToLogin)
        self.loginBtn.clicked.connect(MainWindow.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec_())
