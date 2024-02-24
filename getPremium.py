from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from datetime import datetime
import MySQLdb as mdb

class Ui_PremRegWindow(object):
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
        
    def receive_id(get_id):
        Ui_PremRegWindow.id = get_id
        
    def show_plan(self):
        self.plan.show()
        
    def backToPlans(self):
        self.full_name.clear()
        self.password.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.plan.show()
        
    def show_plan_1(self):
        self.stackedWidget.setCurrentIndex(1)
        db = mdb.connect('localhost','root','','music_app')
        plan = 1
        price = db.cursor()
        duration = db.cursor()
        username = db.cursor()
        email = db.cursor()
        
        price.execute("SELECT `price` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        duration.execute("SELECT `duration` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        username.execute("SELECT `username` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        email.execute("SELECT `email` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        
        get_price = price.fetchone()
        get_duration = duration.fetchone()
        get_username = username.fetchone()
        get_email = email.fetchone()
        
        self.plan_id = plan
        self.price = str(get_price[0])
               
        self.plan_4.setText("Plan " + str(plan))
        self.price_duration.setText(str(get_price[0]) + "VND for " + str(get_duration[0]) + " month.")
        self.label_29.setText("Unlock music pack 1.")
        self.label_30.setText("Download limit of 30 songs.")
        self.username.setText(str(get_username[0]))
        self.email.setText(str(get_email[0]))
        
    def show_plan_2(self):
        self.stackedWidget.setCurrentIndex(1)
        db = mdb.connect('localhost','root','','music_app')
        plan = 2
        price = db.cursor()
        duration = db.cursor()
        username = db.cursor()
        email = db.cursor()
        
        price.execute("SELECT `price` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        duration.execute("SELECT `duration` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        username.execute("SELECT `username` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        email.execute("SELECT `email` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        
        get_price = price.fetchone()
        get_duration = duration.fetchone()
        get_username = username.fetchone()
        get_email = email.fetchone()
        
        self.plan_id = plan
        self.price = str(get_price[0])
               
        self.plan_4.setText("Plan " + str(plan))
        self.price_duration.setText(str(get_price[0]) + "VND for " + str(get_duration[0]) + " month.")
        self.label_29.setText("Unlock music pack 1 and pack 2.")
        self.label_30.setText("Download limit of 60 songs.")
        self.username.setText(str(get_username[0]))
        self.email.setText(str(get_email[0]))
        
    def show_plan_3(self):
        self.stackedWidget.setCurrentIndex(1)
        db = mdb.connect('localhost','root','','music_app')
        plan = 3
        price = db.cursor()
        duration = db.cursor()
        username = db.cursor()
        email = db.cursor()
        
        price.execute("SELECT `price` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        duration.execute("SELECT `duration` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        username.execute("SELECT `username` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        email.execute("SELECT `email` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        
        get_price = price.fetchone()
        get_duration = duration.fetchone()
        get_username = username.fetchone()
        get_email = email.fetchone()
        
        self.plan_id = plan
        self.price = str(get_price[0])
               
        self.plan_4.setText("Plan " + str(plan))
        self.price_duration.setText(str(get_price[0]) + "VND for " + str(get_duration[0]) + " month.")
        self.label_29.setText("Unlock music pack 1, pack 2 and pack 3.")
        self.label_30.setText("Unlimited downloads.")
        self.username.setText(str(get_username[0]))
        self.email.setText(str(get_email[0]))
    
    def show_plan_4(self):
        self.stackedWidget.setCurrentIndex(1)
        db = mdb.connect('localhost','root','','music_app')
        plan = 4
        price = db.cursor()
        duration = db.cursor()
        username = db.cursor()
        email = db.cursor()
        
        price.execute("SELECT `price` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        duration.execute("SELECT `duration` FROM premium_plan WHERE `id` = '"+str(plan)+"'")
        username.execute("SELECT `username` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        email.execute("SELECT `email` FROM user_management WHERE `user_id` = '"+str(Ui_PremRegWindow.id)+"'")
        
        get_price = price.fetchone()
        get_duration = duration.fetchone()
        get_username = username.fetchone()
        get_email = email.fetchone()
        
        self.plan_id = plan
        self.price = str(get_price[0])
               
        self.plan_4.setText("Plan " + str(plan))
        self.price_duration.setText(str(get_price[0]) + "VND for " + str(get_duration[0]) + " month.")
        self.label_29.setText("Unlock all 3 song packs.")
        self.label_30.setText("Download limit of 50 songs.")
        self.username.setText(str(get_username[0]))
        self.email.setText(str(get_email[0]))
        
    def quickPremReg(self):
        full_name = self.full_name.text()
        password = self.password.text()
        current_date = datetime.now().date()
        current_date_str = current_date.strftime("%Y-%m-%d")
        payment_method = None
        if self.credit_card.isChecked():
            payment_method = "Credit card"
        elif self.momo_wallet.isChecked():
            payment_method = "Momo e-wallet"
        db = mdb.connect('localhost','root','','music_app')
        password_db = db.cursor()
        password_db.execute("SELECT `password` FROM user_management WHERE user_id = '"+str(Ui_PremRegWindow.id)+"'")
        get_password = password_db.fetchone()[0]

        if len(full_name) == 0:
            QMessageBox.information(None, "Error", "Please enter your full name")
        elif len(password) == 0:
            QMessageBox.information(None, "Error", "Please enter your password")
        elif password != str(get_password):
            QMessageBox.information(None, "Error", "Password is not match")
        elif not self.credit_card.isChecked() and not self.momo_wallet.isChecked():
            QMessageBox.information(None, "Error", "Please choose a payment method")
        else:
            
            query = db.cursor()
            email = db.cursor()
            email.execute("SELECT `email` FROM user_management WHERE user_id = '"+str(Ui_PremRegWindow.id)+"'")
            payment_gateways = db.cursor()
            payment_gateways.execute("SELECT `id` FROM payment_gateways WHERE name = '"+payment_method+"'")
            get_payment_gateway = payment_gateways.fetchone()[0]
            get_email = email.fetchone()[0]
            QMessageBox.information(None, "Thank you!", "You have successfully registered for the premium package")
            query.execute("INSERT INTO `premium_payment_management` (`user_id`, `payment_gateway_id`, `date`, `fullname`, `email`, `price`, `payment_method`, `plan_id`) VALUES ('"+str(Ui_PremRegWindow.id)+"', '"+str(get_payment_gateway)+"', '"+current_date_str+"', '"+full_name+"', '"+get_email+"', '"+str(self.price)+"', '"+payment_method+"', '"+str(self.plan_id)+"')")
            
            # query.execute("INSERT INTO `premium_payment_management`(`user_id`, `payment_gateway_id`, `date`, `fullname`, `email`, `price`, `payment_method`, `plan_id`) VALUES ('"+str(Ui_PremRegWindow.id)+"','"+str(get_payment_gateway)+"','"+current_date_str+"','"+full_name+"','"+str(get_email)+"','"+self.price+"','"+payment_method+"','"+self.plan_id+"')")
            query.execute("UPDATE `user_management` SET premium = '"+str(1)+"' WHERE user_id = '"+str(Ui_PremRegWindow.id)+"'")
            db.commit()
            QMessageBox.information(None, "Thank you!", "Please login again to continue")
            self.goToLogin()
            
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
        MainWindow.resize(1209, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"border:none;\n"
"padding: 0px;\n"
"margin:0 px;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"#register_2, #confirm{\n"
"background-color: black\n"
"}\n"
"\n"
"#header {\n"
"background-color:#9c2feb;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"#plan {\n"
"background-color:#efefef;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"#plan_1, #plan_2, #plan_3{\n"
"background-color: white;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#register_2 QPushButton{\n"
"color:white;\n"
"background-color:black;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"}\n"
"\n"
"#register_2 #view_plan{\n"
"color:white;\n"
"background-color:#9c2feb;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"}\n"
"\n"
"#register_2 #back{\n"
"color:white;\n"
"background-color:black;\n"
"border-radius:20px;\n"
"padding:10px\n"
"}\n"
"\n"
"#plan QLabel{\n"
"color:black;\n"
"}\n"
"\n"
"#pack_1, #pack_2, #pack_3, #widget_13{\n"
"border-top: 1px solid black\n"
"}\n"
"\n"
"#view_plan {\n"
"background-color:#9c2feb;\n"
"color:white;\n"
"border:1.5px solid white\n"
"}\n"
"\n"
"#premium_plan {\n"
"background-color:white;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"#premium_plan QLabel{\n"
"color:black\n"
"}\n"
"\n"
"#user_in4 {\n"
"background-color:#1f1f1f;\n"
"border-radius:8px;\n"
"color:white\n"
"}\n"
"\n"
"#user_in4 QLabel{\n"
"color:white\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:#121212;\n"
"border-radius: 20px;\n"
"border: 1px solid white;\n"
"padding: 10px;\n"
"color:white;\n"
"}\n"
"\n"
"#user_in4 #finish{\n"
"color:white;\n"
"background-color:black;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"}\n"
"\n"
"#user_in4 #cancel{\n"
"color:white;\n"
"background-color:black;\n"
"border:1px solid white;\n"
"padding:10px;\n"
"border-radius:10px\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.register_2 = QtWidgets.QWidget()
        self.register_2.setObjectName("register_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.register_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QWidget(self.register_2)
        self.header.setObjectName("header")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_10 = QtWidgets.QWidget(self.header)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.back = QtWidgets.QPushButton(self.widget_10)
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources3.qrc/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName("back")
        self.verticalLayout_10.addWidget(self.back, 0, QtCore.Qt.AlignLeft)
        self.label_23 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_10.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.verticalLayout_9.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.header)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setContentsMargins(50, 20, 50, 20)
        self.horizontalLayout_11.setSpacing(300)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.get_started = QtWidgets.QPushButton(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.get_started.setFont(font)
        self.get_started.setObjectName("get_started")
        self.horizontalLayout_11.addWidget(self.get_started)
        self.view_plan = QtWidgets.QPushButton(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.view_plan.setFont(font)
        self.view_plan.setObjectName("view_plan")
        self.horizontalLayout_11.addWidget(self.view_plan)
        self.verticalLayout_9.addWidget(self.widget_11)
        self.verticalLayout_2.addWidget(self.header)
        self.plan = QtWidgets.QWidget(self.register_2)
        self.plan.setObjectName("plan")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.plan)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plan_1 = QtWidgets.QWidget(self.plan)
        self.plan_1.setMinimumSize(QtCore.QSize(0, 300))
        self.plan_1.setSizeIncrement(QtCore.QSize(0, 300))
        self.plan_1.setObjectName("plan_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.plan_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sliver_pack = QtWidgets.QLabel(self.plan_1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sliver_pack.setFont(font)
        self.sliver_pack.setObjectName("sliver_pack")
        self.verticalLayout_3.addWidget(self.sliver_pack)
        self.label_2 = QtWidgets.QLabel(self.plan_1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.pack_1 = QtWidgets.QWidget(self.plan_1)
        self.pack_1.setMinimumSize(QtCore.QSize(0, 250))
        self.pack_1.setObjectName("pack_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pack_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.pack_1)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_6.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(self.pack_1)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14, 0, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.widget_2, 0, QtCore.Qt.AlignLeft)
        self.widget_3 = QtWidgets.QWidget(self.pack_1)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.widget_3, 0, QtCore.Qt.AlignLeft)
        self.get_started_2 = QtWidgets.QPushButton(self.pack_1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.get_started_2.setFont(font)
        self.get_started_2.setObjectName("get_started_2")
        self.verticalLayout_6.addWidget(self.get_started_2)
        self.verticalLayout_3.addWidget(self.pack_1)
        self.horizontalLayout.addWidget(self.plan_1)
        self.plan_2 = QtWidgets.QWidget(self.plan)
        self.plan_2.setMinimumSize(QtCore.QSize(0, 300))
        self.plan_2.setObjectName("plan_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.plan_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gold_pack = QtWidgets.QLabel(self.plan_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.gold_pack.setFont(font)
        self.gold_pack.setObjectName("gold_pack")
        self.verticalLayout_4.addWidget(self.gold_pack)
        self.label_5 = QtWidgets.QLabel(self.plan_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.pack_2 = QtWidgets.QWidget(self.plan_2)
        self.pack_2.setMinimumSize(QtCore.QSize(0, 250))
        self.pack_2.setObjectName("pack_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pack_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_4 = QtWidgets.QWidget(self.pack_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.widget_4, 0, QtCore.Qt.AlignLeft)
        self.widget_5 = QtWidgets.QWidget(self.pack_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_7.addWidget(self.widget_5, 0, QtCore.Qt.AlignLeft)
        self.widget_6 = QtWidgets.QWidget(self.pack_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.widget_6)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_7.addWidget(self.widget_6, 0, QtCore.Qt.AlignLeft)
        self.get_started_3 = QtWidgets.QPushButton(self.pack_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.get_started_3.setFont(font)
        self.get_started_3.setObjectName("get_started_3")
        self.verticalLayout_7.addWidget(self.get_started_3)
        self.verticalLayout_4.addWidget(self.pack_2)
        self.horizontalLayout.addWidget(self.plan_2)
        self.plan_3 = QtWidgets.QWidget(self.plan)
        self.plan_3.setMinimumSize(QtCore.QSize(0, 0))
        self.plan_3.setObjectName("plan_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.plan_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.diamond_pack = QtWidgets.QLabel(self.plan_3)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.diamond_pack.setFont(font)
        self.diamond_pack.setObjectName("diamond_pack")
        self.verticalLayout_5.addWidget(self.diamond_pack)
        self.label_8 = QtWidgets.QLabel(self.plan_3)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignTop)
        self.pack_3 = QtWidgets.QWidget(self.plan_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack_3.sizePolicy().hasHeightForWidth())
        self.pack_3.setSizePolicy(sizePolicy)
        self.pack_3.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("MT Extra")
        self.pack_3.setFont(font)
        self.pack_3.setObjectName("pack_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pack_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_7 = QtWidgets.QWidget(self.pack_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.widget_7)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_9 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.verticalLayout_8.addWidget(self.widget_7, 0, QtCore.Qt.AlignLeft)
        self.widget_8 = QtWidgets.QWidget(self.pack_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.widget_8)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.label_11 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.verticalLayout_8.addWidget(self.widget_8, 0, QtCore.Qt.AlignLeft)
        self.widget_9 = QtWidgets.QWidget(self.pack_3)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.widget_9)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.label_12 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.verticalLayout_8.addWidget(self.widget_9, 0, QtCore.Qt.AlignLeft)
        self.get_started_4 = QtWidgets.QPushButton(self.pack_3)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.get_started_4.setFont(font)
        self.get_started_4.setObjectName("get_started_4")
        self.verticalLayout_8.addWidget(self.get_started_4)
        self.verticalLayout_5.addWidget(self.pack_3)
        self.horizontalLayout.addWidget(self.plan_3)
        self.verticalLayout_2.addWidget(self.plan)
        self.stackedWidget.addWidget(self.register_2)
        self.confirm = QtWidgets.QWidget()
        self.confirm.setObjectName("confirm")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.confirm)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_12 = QtWidgets.QWidget(self.confirm)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setContentsMargins(100, 70, 100, 70)
        self.horizontalLayout_12.setSpacing(100)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.premium_plan = QtWidgets.QWidget(self.widget_12)
        self.premium_plan.setObjectName("premium_plan")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.premium_plan)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_32 = QtWidgets.QLabel(self.premium_plan)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_12.addWidget(self.label_32)
        self.plan_4 = QtWidgets.QLabel(self.premium_plan)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.plan_4.setFont(font)
        self.plan_4.setObjectName("plan_4")
        self.verticalLayout_12.addWidget(self.plan_4)
        self.price_duration = QtWidgets.QLabel(self.premium_plan)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.price_duration.setFont(font)
        self.price_duration.setObjectName("price_duration")
        self.verticalLayout_12.addWidget(self.price_duration)
        self.widget_13 = QtWidgets.QWidget(self.premium_plan)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 350))
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_28 = QtWidgets.QLabel(self.widget_14)
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_13.addWidget(self.label_28)
        self.label_31 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_13.addWidget(self.label_31)
        self.verticalLayout_13.addWidget(self.widget_14, 0, QtCore.Qt.AlignLeft)
        self.widget_15 = QtWidgets.QWidget(self.widget_13)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_26 = QtWidgets.QLabel(self.widget_15)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_14.addWidget(self.label_26)
        self.label_29 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_14.addWidget(self.label_29)
        self.verticalLayout_13.addWidget(self.widget_15, 0, QtCore.Qt.AlignLeft)
        self.widget_16 = QtWidgets.QWidget(self.widget_13)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_27 = QtWidgets.QLabel(self.widget_16)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("resources3.qrc/check.png"))
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_15.addWidget(self.label_27)
        self.label_30 = QtWidgets.QLabel(self.widget_16)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_15.addWidget(self.label_30)
        self.verticalLayout_13.addWidget(self.widget_16, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_12.addWidget(self.widget_13)
        self.horizontalLayout_12.addWidget(self.premium_plan)
        self.user_in4 = QtWidgets.QWidget(self.widget_12)
        self.user_in4.setObjectName("user_in4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.user_in4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_33 = QtWidgets.QLabel(self.user_in4)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_14.addWidget(self.label_33)
        self.widget_17 = QtWidgets.QWidget(self.user_in4)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_34 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_16.addWidget(self.label_34)
        self.full_name = QtWidgets.QLineEdit(self.widget_17)
        self.full_name.setMinimumSize(QtCore.QSize(200, 0))
        self.full_name.setObjectName("full_name")
        self.horizontalLayout_16.addWidget(self.full_name, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_14.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.user_in4)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_35 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_17.addWidget(self.label_35)
        self.username = QtWidgets.QLineEdit(self.widget_18)
        self.username.setMinimumSize(QtCore.QSize(200, 0))
        self.username.setObjectName("username")
        self.horizontalLayout_17.addWidget(self.username, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_14.addWidget(self.widget_18)
        self.widget_19 = QtWidgets.QWidget(self.user_in4)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_36 = QtWidgets.QLabel(self.widget_19)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_18.addWidget(self.label_36)
        self.email = QtWidgets.QLineEdit(self.widget_19)
        self.email.setMinimumSize(QtCore.QSize(200, 0))
        self.email.setObjectName("email")
        self.horizontalLayout_18.addWidget(self.email, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_14.addWidget(self.widget_19)
        self.widget_20 = QtWidgets.QWidget(self.user_in4)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_37 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_19.addWidget(self.label_37)
        self.password = QtWidgets.QLineEdit(self.widget_20)
        self.password.setMinimumSize(QtCore.QSize(200, 0))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_19.addWidget(self.password, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_14.addWidget(self.widget_20)
        self.widget_22 = QtWidgets.QWidget(self.user_in4)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_39 = QtWidgets.QLabel(self.widget_22)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_21.addWidget(self.label_39)
        self.credit_card = QtWidgets.QRadioButton(self.widget_22)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.credit_card.setFont(font)
        self.credit_card.setObjectName("credit_card")
        self.horizontalLayout_21.addWidget(self.credit_card)
        self.momo_wallet = QtWidgets.QRadioButton(self.widget_22)
        self.momo_wallet.setObjectName("momo_wallet")
        self.horizontalLayout_21.addWidget(self.momo_wallet)
        self.verticalLayout_14.addWidget(self.widget_22)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.cancel = QtWidgets.QPushButton(self.user_in4)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_20.addWidget(self.cancel)
        self.finish = QtWidgets.QPushButton(self.user_in4)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.finish.setFont(font)
        self.finish.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-radius:8px")
        self.finish.setObjectName("finish")
        self.horizontalLayout_20.addWidget(self.finish)
        self.verticalLayout_14.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_12.addWidget(self.user_in4)
        self.verticalLayout_11.addWidget(self.widget_12)
        self.stackedWidget.addWidget(self.confirm)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_23.setText(_translate("MainWindow", "69.000VND for 3 months of Premium"))
        self.label_24.setText(_translate("MainWindow", "Enjoy ad-free music listening, unlock all 3 music packs. Cancel anytime."))
        self.get_started.setText(_translate("MainWindow", "Get Started"))
        self.view_plan.setText(_translate("MainWindow", "View plans"))
        self.sliver_pack.setText(_translate("MainWindow", "Plan 1"))
        self.label_2.setText(_translate("MainWindow", "29.000VND for 1 month"))
        self.label.setText(_translate("MainWindow", "Ad-free music listening"))
        self.label_3.setText(_translate("MainWindow", "Unlock music pack 1"))
        self.label_4.setText(_translate("MainWindow", "Download limit of 30 songs"))
        self.get_started_2.setText(_translate("MainWindow", "Get Started"))
        self.gold_pack.setText(_translate("MainWindow", "Plan 2"))
        self.label_5.setText(_translate("MainWindow", "59.000VND for 3 months"))
        self.label_6.setText(_translate("MainWindow", "Ad-free music listening"))
        self.label_7.setText(_translate("MainWindow", "Unlock music pack 1 and pack 2"))
        self.label_10.setText(_translate("MainWindow", "Download limit of 60 songs"))
        self.get_started_3.setText(_translate("MainWindow", "Get Started"))
        self.diamond_pack.setText(_translate("MainWindow", "Plan 3"))
        self.label_8.setText(_translate("MainWindow", "99.000 for 6 months"))
        self.label_9.setText(_translate("MainWindow", "Ad-free music listening"))
        self.label_11.setText(_translate("MainWindow", "Unlock music pack 1, pack 2 and pack 3"))
        self.label_12.setText(_translate("MainWindow", "Unlimited downloads"))
        self.get_started_4.setText(_translate("MainWindow", "Get Started"))
        self.label_32.setText(_translate("MainWindow", "Premium plan of your choice:"))
        self.plan_4.setText(_translate("MainWindow", "Plan 1"))
        self.price_duration.setText(_translate("MainWindow", "29.000VND for 1 month"))
        self.label_31.setText(_translate("MainWindow", "Ad-free music listening"))
        self.label_29.setText(_translate("MainWindow", "Unlock music pack 1"))
        self.label_30.setText(_translate("MainWindow", "Download limit of 30 songs"))
        self.label_33.setText(_translate("MainWindow", "Confirm"))
        self.label_34.setText(_translate("MainWindow", "Full name:"))
        self.full_name.setPlaceholderText(_translate("MainWindow", "Enter your full name"))
        self.label_35.setText(_translate("MainWindow", "Username:"))
        self.label_36.setText(_translate("MainWindow", "Email:"))
        self.label_37.setText(_translate("MainWindow", "Password:"))
        self.password.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.label_39.setText(_translate("MainWindow", "Payment method:"))
        self.credit_card.setText(_translate("MainWindow", "Credit card"))
        self.momo_wallet.setText(_translate("MainWindow", "Momo e-wallet"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.finish.setText(_translate("MainWindow", "Finish"))
        
        self.plan.hide()
        self.view_plan.clicked.connect(self.show_plan)
        self.get_started.clicked.connect(self.show_plan_4)
        self.finish.clicked.connect(self.quickPremReg)
        self.cancel.clicked.connect(self.backToPlans)
        self.back.clicked.connect(self.backToHome)
        self.get_started_2.clicked.connect(self.show_plan_1)
        self.get_started_3.clicked.connect(self.show_plan_2)
        self.get_started_4.clicked.connect(self.show_plan_3)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PremRegWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
