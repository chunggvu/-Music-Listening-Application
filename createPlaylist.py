from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import MySQLdb as mdb


class Ui_CreatePlaylistWindow(object):
    id = 0
    
    def receiveId(get_id):
        Ui_CreatePlaylistWindow.id = get_id
    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()
            
    def createPlaylist(self):
        playlist_name = self.name.text()
        
        if len(playlist_name) != 0:
            db = mdb.connect('localhost','root','','music_app')
            query = db.cursor()
            
            update_query = "INSERT INTO `playlist_management` (`playlist_name`, `user_id`) VALUES (%s, %s)"
            query.execute(update_query, (playlist_name, str(Ui_CreatePlaylistWindow.id),))
                    
            db.commit()
            db.close()
            QMessageBox.information(None, "Success!", "Create successful!")
            self.closeWindows()
        else:
            QMessageBox.critical(None, "Error!", "Please enter your playlist's name")
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.horizontalLayout_2.addWidget(self.submit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create playlist"))
        self.label_2.setText(_translate("MainWindow", "Playlist\'s name:"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        
        self.submit.clicked.connect(self.createPlaylist)
        self.cancel.clicked.connect(self.closeWindows)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CreatePlaylistWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
