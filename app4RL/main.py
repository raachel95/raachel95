# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 640))
        MainWindow.setMaximumSize(QtCore.QSize(850, 640))
        font = QtGui.QFont()
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/ecust.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/ecust.png"))
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 10, 571, 51))
        self.title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.resetButt = QtWidgets.QPushButton(self.centralwidget)
        self.resetButt.setGeometry(QtCore.QRect(600, 350, 131, 41))
        self.resetButt.setObjectName("resetButt")
        self.uploadbutt = QtWidgets.QPushButton(self.centralwidget)
        self.uploadbutt.setGeometry(QtCore.QRect(580, 410, 171, 41))
        self.uploadbutt.setObjectName("uploadbutt")
        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(580, 470, 171, 41))
        self.startButt.setObjectName("startButt")
        self.stopButt = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt.setGeometry(QtCore.QRect(580, 530, 171, 41))
        self.stopButt.setObjectName("stopButt")
        self.frameGante = QtWidgets.QFrame(self.centralwidget)
        self.frameGante.setGeometry(QtCore.QRect(30, 80, 471, 311))
        self.frameGante.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameGante.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameGante.setObjectName("frameGante")
        self.parameters = QtWidgets.QTableWidget(self.centralwidget)
        self.parameters.setGeometry(QtCore.QRect(510, 80, 321, 261))
        self.parameters.setObjectName("parameters")
        self.parameters.setColumnCount(0)
        self.parameters.setRowCount(0)
        self.frameData = QtWidgets.QFrame(self.centralwidget)
        self.frameData.setGeometry(QtCore.QRect(30, 430, 471, 141))
        self.frameData.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameData.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameData.setObjectName("frameData")
        self.schedulingGante = QtWidgets.QLabel(self.centralwidget)
        self.schedulingGante.setGeometry(QtCore.QRect(190, 400, 121, 16))
        self.schedulingGante.setObjectName("schedulingGante")
        self.schedulingTable = QtWidgets.QLabel(self.centralwidget)
        self.schedulingTable.setGeometry(QtCore.QRect(190, 580, 121, 16))
        self.schedulingTable.setObjectName("schedulingTable")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(770, 570, 61, 41))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "xx智能生产调度处理工具"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#003588;\">xx智能生产调度处理工具主界面</span></p></body></html>"))
        self.resetButt.setText(_translate("MainWindow", "重置炉群状态"))
        self.uploadbutt.setText(_translate("MainWindow", "上传炉群数据（单位：天）"))
        self.startButt.setText(_translate("MainWindow", "开启炉群调度（单位：天）"))
        self.stopButt.setText(_translate("MainWindow", "停止"))
        self.schedulingGante.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">调度甘特图</p></body></html>"))
        self.schedulingTable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">调度工作数据表</p></body></html>"))
        self.exit.setText(_translate("MainWindow", "退出"))
