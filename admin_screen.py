from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()
            
    def goToUserManagement(self):
        try:
            from user_management import Ui_UserManagementWindow
            self.user_management_window = QtWidgets.QMainWindow()
            self.ui = Ui_UserManagementWindow()
            self.ui.setupUi(self.user_management_window)
            self.user_management_window.show()
            self.ui.loadAccountData()
            self.ui.loadPaymentData()
            self.closeWindows()
        except ImportError:
            pass
    
    def goToSongManagement(self):
        try:
            from song_management import Ui_SongManagementWindow
            self.song_management_window = QtWidgets.QMainWindow()
            self.ui = Ui_SongManagementWindow()
            self.ui.setupUi(self.song_management_window)
            self.song_management_window.show()
            self.ui.loadSongData()
            self.ui.loadArtistData()
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
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("*{\n"
"    font: 75 14pt \"Arial\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome, admin"))
        self.pushButton.setText(_translate("MainWindow", "User management"))
        self.pushButton_2.setText(_translate("MainWindow", "Song management"))
        self.pushButton_3.setText(_translate("MainWindow", "Back"))
        
        self.pushButton.clicked.connect(self.goToUserManagement)
        self.pushButton_2.clicked.connect(self.goToSongManagement)
        self.pushButton_3.clicked.connect(self.backToHome)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
