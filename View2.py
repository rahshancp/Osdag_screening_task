from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3



class Ui_NewData2(object):

    def setupUi(self, NewData, sor):
        conn = sqlite3.connect('steel_sections.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM Beams")

        allSQLRows = c.fetchall()
        print(allSQLRows[sor][2])
        #print(', '.join(allSQLRows[0]))
        alltest = c.fetchone()
        NewData.setObjectName("NewData")
        NewData.resize(699, 574)
        NewData.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(NewData)
        self.centralwidget.setObjectName("centralwidget")


        # self.Cancel.clicked.connect(self.destroy())
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 231, 31))
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit.setText(str(allSQLRows[sor][1]))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 231, 31))
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(str(allSQLRows[sor][2]))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 130, 231, 31))
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(str(allSQLRows[sor][3]))
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 180, 231, 31))
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(str(allSQLRows[sor][4]))
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 230, 231, 31))
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(str(allSQLRows[sor][5]))
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 280, 231, 31))
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(str(allSQLRows[sor][6]))
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 330, 231, 31))
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText(str(allSQLRows[sor][7]))
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 380, 231, 31))
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setText(str(allSQLRows[sor][8]))
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 430, 231, 31))
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(str(allSQLRows[sor][9]))
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 480, 231, 31))
        self.lineEdit_10.setClearButtonEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(str(allSQLRows[sor][10]))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 390, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 490, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 440, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(460, 430, 231, 31))
        self.lineEdit_18.setClearButtonEnabled(False)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_18.setText(str(allSQLRows[sor][18]))
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(460, 130, 231, 31))
        self.lineEdit_12.setClearButtonEnabled(False)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText(str(allSQLRows[sor][12]))
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(400, 240, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(460, 80, 231, 31))
        self.lineEdit_11.setClearButtonEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText(str(allSQLRows[sor][11]))
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(460, 180, 231, 31))
        self.lineEdit_13.setClearButtonEnabled(False)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(str(allSQLRows[sor][13]))
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(400, 490, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(460, 330, 231, 31))
        self.lineEdit_16.setClearButtonEnabled(False)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setText(str(allSQLRows[sor][16]))
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(460, 380, 231, 31))
        self.lineEdit_17.setClearButtonEnabled(False)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.setText(str(allSQLRows[sor][17]))
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(400, 390, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(400, 440, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(400, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(460, 480, 231, 31))
        self.lineEdit_19.setClearButtonEnabled(False)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_19.setText(str(allSQLRows[sor][19]))
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(460, 230, 231, 31))
        self.lineEdit_14.setClearButtonEnabled(False)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText(str(allSQLRows[sor][14]))
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(460, 280, 231, 31))
        self.lineEdit_15.setClearButtonEnabled(False)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setText(str(allSQLRows[sor][15]))
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(400, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(400, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        NewData.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewData)
        self.statusbar.setObjectName("statusbar")
        NewData.setStatusBar(self.statusbar)


        self.retranslateUi(NewData)
        QtCore.QMetaObject.connectSlotsByName(NewData)

    def retranslateUi(self, NewData):
        _translate = QtCore.QCoreApplication.translate
        NewData.setWindowTitle(_translate("NewData", "New Data"))


        self.label.setText(_translate("NewData", "Designation"))
        self.label_2.setText(_translate("NewData", "Mass"))
        self.label_3.setText(_translate("NewData", "Area"))
        self.label_4.setText(_translate("NewData", "D"))
        self.label_5.setText(_translate("NewData", "B"))
        self.label_6.setText(_translate("NewData", "tw"))
        self.label_7.setText(_translate("NewData", "Flangeslope"))
        self.label_8.setText(_translate("NewData", "R2"))
        self.label_9.setText(_translate("NewData", "T"))
        self.label_10.setText(_translate("NewData", "R1"))
        self.label_11.setText(_translate("NewData", "Zy"))
        self.label_12.setText(_translate("NewData", "ry"))
        self.label_13.setText(_translate("NewData", "ly"))
        self.label_14.setText(_translate("NewData", "Source"))
        self.label_15.setText(_translate("NewData", "Zpz"))
        self.label_16.setText(_translate("NewData", "Zpy"))
        self.label_17.setText(_translate("NewData", "lz"))
        self.label_18.setText(_translate("NewData", "Zz"))
        self.label_19.setText(_translate("NewData", "rz"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    NewData = QtWidgets.QMainWindow()
    ui = Ui_NewData2()
    ui.setupUi(NewData)
    NewData.show()

    sys.exit(app.exec_())