from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem, QTableView



from Append import Ui_NewData
from View2 import Ui_NewData2


class Ui_MainWindow(object):

    def appendW(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewData()
        self.ui.setupUi(self.window)
        self.window.show()

    def oncclick(self):
        print("\n")
        #
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            #ctypes.windll.user32.MessageBoxW(0, "dggdfg "+ currentQTableWidgetItem.text(), "Your title", 1)
            #soi = currentQTableWidgetItem.text()
            sor = currentQTableWidgetItem.row()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_NewData2()
            self.ui.setupUi(self.window, sor)
            self.window.show()



    def setupUi(self, MainWindow):
        conn = sqlite3.connect('steel_sections.sqlite')
        c = conn.cursor()
        dodo = ("JB 200")
        c.execute('SELECT designation FROM Beams')

        allSQLRows = c.fetchall()
        #print(', '.join(allSQLRows[0]))
        alltest = c.fetchone()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 110, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(allSQLRows))
        rowx=0
        for x in allSQLRows:
            self.tableWidget.setItem(0, rowx, QTableWidgetItem(str(', '.join(x))))
            rowx +=1
        self.tableWidget.clicked.connect(self.oncclick)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 380, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.appendW)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #@pyqtSlot()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add new"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
