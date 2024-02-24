from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import MySQLdb as mdb

class Ui_ProfileWindow(object):
    id = 0
    
    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()
    
    def receive_id(get_id):
        Ui_ProfileWindow.id = get_id
        
    def logout(self): 
        try:
            from homeScreen0 import Ui_MainWindow
            self.home_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.home_window)
            self.home_window.show()
            self.closeWindows()
        except ImportError:
            pass
        
    def backToHome(self): 
        try:
            from homeScreen1 import Ui_HomeWindow
            self.home_window = QtWidgets.QMainWindow()
            self.ui = Ui_HomeWindow()
            self.ui.setupUi(self.home_window)
            self.home_window.show()
            self.ui.load_song()
            self.closeWindows()
        except ImportError:
            pass
    
    def goToManagement(self):
        try:
            from admin_screen import Ui_AdminWindow
            self.admin_window = QtWidgets.QMainWindow()
            self.ui = Ui_AdminWindow()
            self.ui.setupUi(self.admin_window)
            self.admin_window.show()
            self.ui.label.setText(f"Welcome, {self.admin}")
            self.closeWindows()
        except ImportError:
            pass
        
    def changePass(self):
        try:
            from changePass import Ui_ChangePasswordWindow
            self.change_password_window = QtWidgets.QMainWindow()
            self.ui = Ui_ChangePasswordWindow()
            self.ui.setupUi(self.change_password_window)
            self.change_password_window.show()
            senIDToChangePass = Ui_ChangePasswordWindow
            senIDToChangePass.receiveId(str(Ui_ProfileWindow.id))
        except ImportError:
            pass
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 661)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: #1f1f1f;\n"
"}\n"
"\n"
"#username {\n"
"font: 25pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"#profile_image {\n"
"border: 0px;\n"
"width:100px;\n"
"height:100px\n"
"}\n"
"\n"
"#widget #logout_btn{\n"
"background-color:white;\n"
"color:black;\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#widget #back_btn{\n"
"background-color:white;\n"
"color:black;\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#widget_2 #change_password{\n"
"background-color:#1f1f1f;\n"
"color:white;\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#goToAdmin{\n"
"background-color:white;\n"
"color:black;\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#profile_image{\n"
"border:none;\n"
"}\n"
"\n"
"#top_artist_list{\n"
"background-color:#1f1f1f;\n"
"border:none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.widget)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn, 0, QtCore.Qt.AlignLeft)
        self.logout_btn = QtWidgets.QPushButton(self.widget)
        self.logout_btn.setObjectName("logout_btn")
        self.horizontalLayout.addWidget(self.logout_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.profile_image = QtWidgets.QPushButton(self.widget_2)
        self.profile_image.setMinimumSize(QtCore.QSize(0, 0))
        self.profile_image.setMaximumSize(QtCore.QSize(200, 200))
        self.profile_image.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources3.qrc/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_image.setIcon(icon)
        self.profile_image.setIconSize(QtCore.QSize(200, 200))
        self.profile_image.setObjectName("profile_image")
        self.horizontalLayout_2.addWidget(self.profile_image)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.username = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.verticalLayout_2.addWidget(self.username)
        self.change_password = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.change_password.setFont(font)
        self.change_password.setObjectName("change_password")
        self.verticalLayout_2.addWidget(self.change_password, 0, QtCore.Qt.AlignLeft)
        self.goToAdmin = QtWidgets.QPushButton(self.widget_2)
        self.goToAdmin.setMaximumSize(QtCore.QSize(200, 200))
        self.goToAdmin.setObjectName("goToAdmin")
        self.verticalLayout_2.addWidget(self.goToAdmin, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.top_artist_list = QtWidgets.QListWidget(self.widget_3)
        self.top_artist_list.setObjectName("top_artist_list")
        self.verticalLayout_4.addWidget(self.top_artist_list)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.logout_btn.setText(_translate("MainWindow", "Log out"))
        self.label_3.setText(_translate("MainWindow", "Profile"))
        self.username.setText(_translate("MainWindow", "Username"))
        self.change_password.setText(_translate("MainWindow", "Change password"))
        self.goToAdmin.setText(_translate("MainWindow", "Go to management"))
                
        db = mdb.connect('localhost','root','','music_app')
        db_username = db.cursor()
        db_username.execute("SELECT username FROM user_management WHERE user_id = '"+str(Ui_ProfileWindow.id)+"'")
       
        get_username = db_username.fetchone()[0]
        self.admin = get_username
        self.username.setText(str(get_username))
        
        role = db.cursor()
        role.execute("SELECT role FROM user_management WHERE user_id = '"+str(Ui_ProfileWindow.id)+"'")
        get_role = role.fetchone()[0]
        
        if get_role == 0:
            self.goToAdmin.hide()
            self.goToAdmin.setEnabled(False)
        else:
            self.goToAdmin.show()
            self.goToAdmin.setEnabled(True)
        
        
        self.logout_btn.clicked.connect(self.logout)
        self.back_btn.clicked.connect(self.backToHome)
        self.change_password.clicked.connect(self.changePass)
        self.goToAdmin.clicked.connect(self.goToManagement)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
