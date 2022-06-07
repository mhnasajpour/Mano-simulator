# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import images


class Ui_information_window(object):
    def setupUi(self):
        # information_window.setObjectName("information_window")
        # information_window.resize(1390, 800)
        # information_window.setStyleSheet("background-image: url(:/images/images/back1.png);")
        self.about_project_text = QtWidgets.QPlainTextEdit()
        self.about_project_text.setGeometry(QtCore.QRect(310, 290, 821, 91))
        self.about_project_text.setStyleSheet("background: #0000ffff;\n"
                                              "color: #afc5d0;\n"
                                              "font: 75 10.5pt \"MS Shell Dlg 2\";\n"
                                              "")
        self.about_project_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.about_project_text.setReadOnly(True)
        self.about_project_text.setObjectName("about_project_text")
        self.computer_label = QtWidgets.QLabel()
        self.computer_label.setGeometry(QtCore.QRect(260, 230, 61, 51))
        self.computer_label.setStyleSheet("background: #0000ffff;\n"
                                          "background-image: url(:/images/images/copmuter.png);\n"
                                          "background-repeat: no-repeat;")
        self.computer_label.setText("")
        self.computer_label.setObjectName("computer_label")
        self.team_label = QtWidgets.QLabel()
        self.team_label.setGeometry(QtCore.QRect(270, 420, 61, 51))
        self.team_label.setStyleSheet("background: #0000ffff;\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-image: url(:/images/images/team.png);")
        self.team_label.setText("")
        self.team_label.setObjectName("team_label")
        self.github_icon_1 = QtWidgets.QLabel()
        self.github_icon_1.setGeometry(QtCore.QRect(310, 490, 41, 41))
        self.github_icon_1.setStyleSheet("background: #0000ffff;\n"
                                         "background-repeat: no-repeat;\n"
                                         "background-image: url(:/images/images/github.png);")
        self.github_icon_1.setText("")
        self.github_icon_1.setObjectName("github_icon_1")
        self.github_icon_2 = QtWidgets.QLabel()
        self.github_icon_2.setGeometry(QtCore.QRect(610, 490, 41, 41))
        self.github_icon_2.setStyleSheet("background: #0000ffff;\n"
                                         "background-image: url(:/images/images/github.png);\n"
                                         "background-repeat: no-repeat;")
        self.github_icon_2.setText("")
        self.github_icon_2.setObjectName("github_icon_2")
        self.github_icon_3 = QtWidgets.QLabel()
        self.github_icon_3.setGeometry(QtCore.QRect(860, 490, 41, 41))
        self.github_icon_3.setStyleSheet("background: #0000ffff;\n"
                                         "background-repeat: no-repeat;\n"
                                         "background-image: url(:/images/images/github.png);")
        self.github_icon_3.setText("")
        self.github_icon_3.setObjectName("github_icon_3")
        self.name_2 = QtWidgets.QPlainTextEdit()
        self.name_2.setGeometry(QtCore.QRect(650, 490, 181, 71))
        self.name_2.setStyleSheet("background: #0000ffff;\n"
                                  "color: #afc5d0;\n"
                                  "font: 75 9.5pt \"MS Shell Dlg 2\";\n"
                                  "")
        self.name_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_2.setReadOnly(True)
        self.name_2.setObjectName("name_2")
        self.name_1 = QtWidgets.QPlainTextEdit()
        self.name_1.setGeometry(QtCore.QRect(350, 490, 171, 81))
        self.name_1.setStyleSheet("background: #0000ffff;\n"
                                  "color: #afc5d0;\n"
                                  "font: 75 9.5pt \"MS Shell Dlg 2\";\n"
                                  "")
        self.name_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_1.setReadOnly(True)
        self.name_1.setObjectName("name_1")
        self.name_3 = QtWidgets.QPlainTextEdit()
        self.name_3.setGeometry(QtCore.QRect(900, 490, 211, 71))
        self.name_3.setStyleSheet("background: #0000ffff;\n"
                                  "color: #afc5d0;\n"
                                  "font: 75 9.5pt \"MS Shell Dlg 2\";\n"
                                  "")
        self.name_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_3.setReadOnly(True)
        self.name_3.setObjectName("name_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.about_project_text.setPlainText(_translate(
            "information_window", "This is a Qt & Python application that compiles assembly code for and runs a simulation of Mano\'s Computer as detailed in: Computer System Architecture, 3rd edition by M. Morris Mano Published by Prentice-Hall, c 1993 Chapter 5, pp 123-172."))
        self.name_2.setPlainText(_translate("information_window", "Melika Fotoohi\n"
                                            "MelikaFotoohi"))
        self.name_1.setPlainText(_translate("information_window", "Mohammad Nasajpour\n"
                                            "mhnasajpour"))
        self.name_3.setPlainText(_translate("information_window", "Fatemeh Ghadamzadeh\n"
                                            "ftmh.ghz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_window = QtWidgets.QWidget()
    ui = Ui_information_window()
    ui.setupUi()
    information_window.show()
    sys.exit(app.exec_())
