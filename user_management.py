from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import MySQLdb as mdb

class Ui_UserManagementWindow(object):
    def onTableItemClicked(self, item):
        row = item.row()
        le_id_data = self.account_table.item(row, 0).text()
        le_username_data = self.account_table.item(row, 1).text()
        le_email_data = self.account_table.item(row, 2).text()
        le_password_data = self.account_table.item(row, 3).text()
        le_premium_data = self.account_table.item(row, 4).text()
        le_role_data = self.account_table.item(row, 5).text()
        if le_role_data == "0":
            self.user.setChecked(True)
        elif le_role_data == "1":
            self.admin.setChecked(True)
        
        if le_premium_data == "0":
            self.leFullname.setText("Unknown")
            self.lePlan.setText("0")
            self.leDate.setText("0")
            self.leMethod.setText("None")
            self.lePrice.setText("0")
        elif le_premium_data == "1":
            db = mdb.connect('localhost', 'root', '', 'music_app')
            query = db.cursor()
            query.execute("SELECT `fullname`, `plan_id`, `date`, `payment_method`, `price` FROM premium_payment_management WHERE user_id = '"+le_id_data+"'")
            payment_data = query.fetchone()
            fullname = payment_data[0]
            plan_id = payment_data[1]
            date = payment_data[2]
            method = payment_data[3]
            price = payment_data[4] 
            
            self.leFullname.setText(fullname)
            self.lePlan.setText(str(plan_id))
            self.leDate.setText(str(date))
            self.leMethod.setText(method)
            self.lePrice.setText(str(price))
        
        self.leID.setText(le_id_data)
        self.leUsername.setText(le_username_data)
        self.leEmail.setText(le_email_data) 
        self.lePassword.setText(le_password_data)
        self.lePremium.setText(le_premium_data)
        
    def loadAccountData(self):
        db = mdb.connect('localhost', 'root', '', 'music_app')
        query = db.cursor()
        query.execute("SELECT * FROM user_management")
        result = query.fetchall()
        self.account_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.account_table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.account_table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def loadPaymentData(self):
        db = mdb.connect('localhost', 'root', '', 'music_app')
        query = db.cursor()
        query.execute("SELECT * FROM premium_payment_management")
        result = query.fetchall()
        self.payment_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.payment_table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.payment_table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def updateData(self):
        role = "0"
        if self.user.isChecked():
            role = "0"
        elif self.admin.isChecked():
            role = "1"
        
        user_id = self.leID.text()
        username = self.leUsername.text()
        email = self.leEmail.text()
        password = self.lePassword.text()
        premium = self.lePremium.text()
        
        fullname = self.leFullname.text()
                
        try:
            db = mdb.connect('localhost', 'root', '', 'music_app')
            query_account = db.cursor()
            query_payment = db.cursor()
            
            update_account = "UPDATE `user_management` SET `username`=%s, `email`=%s, `password`=%s, `premium`=%s, `role`=%s WHERE `user_id`=%s"
            query_account.execute(update_account, (username, email, password, premium, role, user_id))
            
            update_payment = "UPDATE `premium_payment_management` SET `fullname`=%s, `email`=%s WHERE `user_id`=%s"
            query_payment.execute(update_payment, (fullname, email, user_id))
            
            db.commit()
            db.close()
            
            QMessageBox.information(None, "Success!", "Update successful!")
            self.loadAccountData()
            self.loadPaymentData()
            
        except mdb.Error as e:
            print(f"Error: {e}")
            QMessageBox.critical(None, "Error", "Update fail!")

    def deleteData(self):
        id_to_delete = self.leID.text()
        premium = self.lePremium.text()
        try:
            db = mdb.connect('localhost', 'root', '', 'music_app')
            query_account = db.cursor()
            query_payment = db.cursor()
            
            delete_account = "DELETE FROM `user_management` WHERE user_id = %s"
            query_account.execute(delete_account, (id_to_delete,))
            
            if premium == "1":
                delete_payment = "DELETE FROM `premium_payment_management` WHERE user_id = %s"
                query_payment.execute(delete_payment, (id_to_delete,))
                
            db.commit()
            db.close()
            
            QMessageBox.information(None, "Success!", "Delete successful!")
            self.leID.clear()
            self.leUsername.clear()
            self.leEmail.clear()
            self.lePassword.clear()
            self.lePremium.clear()
            self.leFullname.clear()
            self.lePlan.clear()
            self.leDate.clear()
            self.leMethod.clear()
            self.lePrice.clear()
            self.user.setChecked(False)
            self.admin.setChecked(False)

            self.loadAccountData()
            self.loadPaymentData()            
        except mdb.Error as e:
            print(f"Error: {e}")
            QMessageBox.critical(None, "Error", "Delete fail!")

    def backToAdmin(self):
        try:
            from admin_screen import Ui_AdminWindow
            self.home_window = QtWidgets.QMainWindow()
            self.ui = Ui_AdminWindow()
            self.ui.setupUi(self.home_window)
            self.home_window.show()
           
            self.closeWindows()
        except ImportError:
            pass

    def closeWindows(self):
        current_window = QtWidgets.QApplication.activeWindow()
        if current_window is not None:
            current_window.close()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1155, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    font: 10pt \"Arial\";\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.account_table = QtWidgets.QTableWidget(self.widget_3)
        self.account_table.setObjectName("account_table")
        self.account_table.setColumnCount(6)
        self.account_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.account_table)
        self.payment_table = QtWidgets.QTableWidget(self.widget_3)
        self.payment_table.setObjectName("payment_table")
        self.payment_table.setColumnCount(9)
        self.payment_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_table.setHorizontalHeaderItem(8, item)
        self.verticalLayout_4.addWidget(self.payment_table)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leID = QtWidgets.QLineEdit(self.widget_4)
        self.leID.setObjectName("leID")
        self.horizontalLayout_2.addWidget(self.leID, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.leUsername = QtWidgets.QLineEdit(self.widget_4)
        self.leUsername.setObjectName("leUsername")
        self.horizontalLayout_3.addWidget(self.leUsername, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.leFullname = QtWidgets.QLineEdit(self.widget_4)
        self.leFullname.setObjectName("leFullname")
        self.horizontalLayout_11.addWidget(self.leFullname, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.leEmail = QtWidgets.QLineEdit(self.widget_4)
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout_4.addWidget(self.leEmail, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lePassword = QtWidgets.QLineEdit(self.widget_4)
        self.lePassword.setObjectName("lePassword")
        self.horizontalLayout_5.addWidget(self.lePassword, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lePremium = QtWidgets.QLineEdit(self.widget_4)
        self.lePremium.setObjectName("lePremium")
        self.horizontalLayout_6.addWidget(self.lePremium, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lePlan = QtWidgets.QLineEdit(self.widget_4)
        self.lePlan.setObjectName("lePlan")
        self.horizontalLayout_9.addWidget(self.lePlan, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.leDate = QtWidgets.QLineEdit(self.widget_4)
        self.leDate.setObjectName("leDate")
        self.horizontalLayout_12.addWidget(self.leDate, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.leMethod = QtWidgets.QLineEdit(self.widget_4)
        self.leMethod.setObjectName("leMethod")
        self.horizontalLayout_13.addWidget(self.leMethod, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.lePrice = QtWidgets.QLineEdit(self.widget_4)
        self.lePrice.setObjectName("lePrice")
        self.horizontalLayout_14.addWidget(self.lePrice, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.admin = QtWidgets.QRadioButton(self.widget_4)
        self.admin.setObjectName("admin")
        self.horizontalLayout_7.addWidget(self.admin)
        self.user = QtWidgets.QRadioButton(self.widget_4)
        self.user.setObjectName("user")
        self.horizontalLayout_7.addWidget(self.user)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.delete_btn = QtWidgets.QPushButton(self.widget_4)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_8.addWidget(self.delete_btn)
        self.update_btn = QtWidgets.QPushButton(self.widget_4)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_8.addWidget(self.update_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USER MANAGEMENT"))
        item = self.account_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.account_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.account_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.account_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.account_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.account_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.account_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.account_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.account_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.account_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Premium"))
        item = self.account_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Role"))
        item = self.payment_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.payment_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.payment_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.payment_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.payment_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.payment_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Payment ID"))
        item = self.payment_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.payment_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fullname"))
        item = self.payment_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.payment_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Plan ID"))
        item = self.payment_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        item = self.payment_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Method"))
        item = self.payment_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Price"))
        item = self.payment_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Gateway ID"))
        self.pushButton_3.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "User ID:"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.label_9.setText(_translate("MainWindow", "Fullname"))
        self.label_4.setText(_translate("MainWindow", "Email:"))
        self.label_5.setText(_translate("MainWindow", "Password:"))
        self.label_6.setText(_translate("MainWindow", "Premium:"))
        self.label_8.setText(_translate("MainWindow", "Plan ID:"))
        self.label_10.setText(_translate("MainWindow", "Date:"))
        self.label_11.setText(_translate("MainWindow", "Method:"))
        self.label_12.setText(_translate("MainWindow", "Price:"))
        self.label_7.setText(_translate("MainWindow", "Role:"))
        self.admin.setText(_translate("MainWindow", "Admin:"))
        self.user.setText(_translate("MainWindow", "User:"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        
        self.leID.setEnabled(False)
        self.lePremium.setEnabled(False)
        self.lePlan.setEnabled(False)
        self.leDate.setEnabled(False)
        self.leMethod.setEnabled(False)
        self.lePrice.setEnabled(False)
        
        self.account_table.itemClicked.connect(self.onTableItemClicked)
        self.update_btn.clicked.connect(self.updateData)
        self.delete_btn.clicked.connect(self.deleteData)
        self.pushButton_3.clicked.connect(self.backToAdmin)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_UserManagementWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
