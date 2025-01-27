# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 687)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setStyleSheet("QGroupBox#groupBox {\n"
"    background-color: #7f7f7f; /* White background */\n"
"    background-color: rgb(213, 213, 213);\n"
"    border-radius: 15px; /* Smooth rounded corners */\n"
"    border: 1px solid #e6e6e6; /* Subtle border */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* Shadow effect */\n"
"    margin-top: 10px; /* Space above the title (if there’s a title) */\n"
"}\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 3, 2, 1, 1)
        self.inputWid = QtWidgets.QWidget(parent=self.groupBox)
        self.inputWid.setMinimumSize(QtCore.QSize(461, 61))
        self.inputWid.setMaximumSize(QtCore.QSize(461, 261))
        self.inputWid.setObjectName("inputWid")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.inputWid)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.filePathField = QtWidgets.QLineEdit(parent=self.inputWid)
        self.filePathField.setMinimumSize(QtCore.QSize(371, 41))
        self.filePathField.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Light gray background */\n"
"    border: 1px solid #dcdcdc; /* Subtle border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 8px; /* Spacing inside the input box */\n"
"    font-size: 14px; /* Adjust font size */\n"
"    color: #333; /* Text color */\n"
"    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #fbbd42; /* Highlighted border when focused */\n"
"    outline: none; /* Remove the default outline */\n"
"}\n"
"\n"
"")
        self.filePathField.setInputMask("")
        self.filePathField.setText("")
        self.filePathField.setReadOnly(True)
        self.filePathField.setObjectName("filePathField")
        self.gridLayout_4.addWidget(self.filePathField, 1, 0, 1, 1)
        self.selectButton = QtWidgets.QToolButton(parent=self.inputWid)
        self.selectButton.setStyleSheet("background: none;\n"
"font: 20pt bold \"Arial\"")
        self.selectButton.setIconSize(QtCore.QSize(32, 32))
        self.selectButton.setObjectName("selectButton")
        self.gridLayout_4.addWidget(self.selectButton, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.passcodeField = QtWidgets.QLineEdit(parent=self.inputWid)
        self.passcodeField.setMinimumSize(QtCore.QSize(371, 41))
        self.passcodeField.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Light gray background */\n"
"    border: 1px solid #dcdcdc; /* Subtle border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 8px; /* Spacing inside the input box */\n"
"    font-size: 14px; /* Adjust font size */\n"
"    color: #333; /* Text color */\n"
"    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #fbbd42; /* Highlighted border when focused */\n"
"    outline: none; /* Remove the default outline */\n"
"}\n"
"\n"
"")
        self.passcodeField.setInputMask("")
        self.passcodeField.setText("")
        self.passcodeField.setObjectName("passcodeField")
        self.gridLayout_4.addWidget(self.passcodeField, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 4, 0, 1, 1)
        self.endecWid = QtWidgets.QWidget(parent=self.inputWid)
        self.endecWid.setObjectName("endecWid")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.endecWid)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.decButton = QtWidgets.QPushButton(parent=self.endecWid)
        self.decButton.setMinimumSize(QtCore.QSize(131, 41))
        self.decButton.setStyleSheet("QPushButton {\n"
"    background-color: #050505; /* Default background color */\n"
"    color: #fafafa; /* Text color */\n"
"    border: 2px solid; /* Remove border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding for the button */\n"
"    font: 10pt \"Roboto\";  /* Font style */\n"
"    box-shadow: none; /* No shadow by default */\n"
"    transition: all 0.5s ease; /* Smooth transition for hover effects */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255); /* Change background color on hover */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* Add shadow on hover */\n"
"    color: #000000; /* Keep text color the same */\n"
"}\n"
"\n"
"")
        self.decButton.setObjectName("decButton")
        self.gridLayout_3.addWidget(self.decButton, 0, 2, 1, 1)
        self.encButton = QtWidgets.QPushButton(parent=self.endecWid)
        self.encButton.setMinimumSize(QtCore.QSize(131, 41))
        self.encButton.setStyleSheet("QPushButton {\n"
"    background-color: #050505; /* Default background color */\n"
"    color: #fafafa; /* Text color */\n"
"    border: 2px solid; /* Remove border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding for the button */\n"
"    font: 10pt \"Roboto\";  /* Font style */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* No shadow by default */\n"
"    transition: all 0.5s ease; /* Smooth transition for hover effects */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255); /* Change background color on hover */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* Add shadow on hover */\n"
"    color: #000000; /* Keep text color the same */\n"
"}\n"
"\n"
"")
        self.encButton.setObjectName("encButton")
        self.gridLayout_3.addWidget(self.encButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.endecWid, 5, 0, 1, 2)
        self.gridLayout_5.addWidget(self.inputWid, 3, 1, 1, 1)
        self.welcomeLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.welcomeLabel.setStyleSheet("font: 14pt \"Lucida Sans\";")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.gridLayout_5.addWidget(self.welcomeLabel, 0, 0, 1, 3)
        self.statLeb = QtWidgets.QLabel(parent=self.groupBox)
        self.statLeb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.statLeb.setObjectName("statLeb")
        self.gridLayout_5.addWidget(self.statLeb, 2, 0, 1, 3)
        self.sideButtonWid = QtWidgets.QWidget(parent=self.groupBox)
        self.sideButtonWid.setObjectName("sideButtonWid")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sideButtonWid)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.histButton = QtWidgets.QPushButton(parent=self.sideButtonWid)
        self.histButton.setMinimumSize(QtCore.QSize(131, 41))
        self.histButton.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; /* Default background color */\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid; /* Remove border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding for the button */\n"
"    font: 10pt \"Roboto\";  /* Font style */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* No shadow by default */\n"
"    transition: all 0.5s ease; /* Smooth transition for hover effects */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(171, 193, 203); /* Change background color on hover */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* Add shadow on hover */\n"
"    color: #fafafa; /* Keep text color the same */\n"
"}\n"
"\n"
"")
        self.histButton.setObjectName("histButton")
        self.horizontalLayout.addWidget(self.histButton)
        spacerItem4 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.logOutButton = QtWidgets.QPushButton(parent=self.sideButtonWid)
        self.logOutButton.setMinimumSize(QtCore.QSize(131, 41))
        self.logOutButton.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; /* Default background color */\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid; /* Remove border */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding for the button */\n"
"    font: 10pt \"Roboto\";  /* Font style */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* No shadow by default */\n"
"    transition: all 0.5s ease; /* Smooth transition for hover effects */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(171, 193, 203); /* Change background color on hover */\n"
"    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25); /* Add shadow on hover */\n"
"    color: #fafafa; /* Keep text color the same */\n"
"}\n"
"\n"
"")
        self.logOutButton.setObjectName("logOutButton")
        self.horizontalLayout.addWidget(self.logOutButton)
        self.gridLayout_5.addWidget(self.sideButtonWid, 4, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 3, 0, 1, 1)
        self.mainMsgLeb = QtWidgets.QLabel(parent=self.groupBox)
        self.mainMsgLeb.setStyleSheet("font: 10pt \"Roboto\";")
        self.mainMsgLeb.setObjectName("mainMsgLeb")
        self.gridLayout_5.addWidget(self.mainMsgLeb, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filePathField.setPlaceholderText(_translate("MainWindow", "No file selected"))
        self.selectButton.setText(_translate("MainWindow", "+"))
        self.passcodeField.setPlaceholderText(_translate("MainWindow", "Passcode"))
        self.decButton.setText(_translate("MainWindow", "Decrypt File"))
        self.encButton.setText(_translate("MainWindow", "Encrypt File"))
        self.welcomeLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.statLeb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.histButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>See the history</p></body></html>"))
        self.histButton.setText(_translate("MainWindow", "History"))
        self.logOutButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Log out</p></body></html>"))
        self.logOutButton.setText(_translate("MainWindow", "Log Out"))
        self.mainMsgLeb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Select your file and then enter a password to encrypt it. </span></p><p align=\"center\">Remember the password otherwise the file won\'t be able to be recovered.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
