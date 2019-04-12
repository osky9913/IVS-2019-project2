# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(421, 431)
        self.centralWidget = QtWidgets.QWidget(Calculator)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 220, 71, 71))
        self.pushButton_4.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 220, 71, 71))
        self.pushButton_5.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 360, 141, 71))
        self.pushButton_0.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 290, 71, 71))
        self.pushButton_1.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 290, 71, 71))
        self.pushButton_2.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_Ans = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Ans.setGeometry(QtCore.QRect(280, 290, 141, 71))
        self.pushButton_Ans.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_Ans.setObjectName("pushButton_Ans")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(140, 360, 71, 71))
        self.pushButton_decimal.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(210, 360, 71, 71))
        self.pushButton_plus.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 290, 71, 71))
        self.pushButton_3.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 220, 71, 71))
        self.pushButton_6.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(210, 290, 71, 71))
        self.pushButton_minus.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 150, 71, 71))
        self.pushButton_9.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 150, 71, 71))
        self.pushButton_7.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 150, 71, 71))
        self.pushButton_8.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(210, 220, 71, 71))
        self.pushButton_mul.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_powr = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_powr.setGeometry(QtCore.QRect(210, 80, 71, 71))
        self.pushButton_powr.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_powr.setObjectName("pushButton_powr")
        self.pushButton_factorial = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_factorial.setGeometry(QtCore.QRect(280, 220, 141, 71))
        self.pushButton_factorial.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.pushButton_evaluate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_evaluate.setGeometry(QtCore.QRect(280, 360, 141, 71))
        self.pushButton_evaluate.setStyleSheet("QPushButton {     color:white;\n"
"                                    border: 1px solid  white; \n"
"                                    background-color: #6ed427;\n"
"                                    font-weight:900;\n"
"} \n"
"\n"
"QPushButton:pressed { background-color: #54a11e; } \n"
"\n"
"")
        self.pushButton_evaluate.setObjectName("pushButton_evaluate")
        self.pushButton_zavorkaP = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zavorkaP.setGeometry(QtCore.QRect(140, 80, 71, 71))
        self.pushButton_zavorkaP.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_zavorkaP.setObjectName("pushButton_zavorkaP")
        self.pushButton_clean = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clean.setGeometry(QtCore.QRect(0, 80, 71, 71))
        self.pushButton_clean.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.pushButton_div = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_div.setGeometry(QtCore.QRect(210, 150, 71, 71))
        self.pushButton_div.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_zavorkaL = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zavorkaL.setGeometry(QtCore.QRect(70, 80, 71, 71))
        self.pushButton_zavorkaL.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_zavorkaL.setObjectName("pushButton_zavorkaL")
        self.pushButton_ln = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ln.setGeometry(QtCore.QRect(280, 150, 71, 71))
        self.pushButton_ln.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.pushButton_root = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_root.setGeometry(QtCore.QRect(280, 80, 71, 71))
        self.pushButton_root.setStyleSheet("QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
"")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_help = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_help.setGeometry(QtCore.QRect(350, 80, 71, 141))
        self.pushButton_help.setObjectName("pushButton_help")
        self.label_vysledek = QtWidgets.QLabel(self.centralWidget)
        self.label_vysledek.setGeometry(QtCore.QRect(0, 0, 421, 41))
        self.label_vysledek.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignLeft\'; border: 1px solid #44bb46; color:white; background-color : #44bb46; font-weight:900; }")
        self.label_vysledek.setText("")
        self.label_vysledek.setObjectName("label_vysledek")
        self.label_zapis = QtWidgets.QLabel(self.centralWidget)
        self.label_zapis.setGeometry(QtCore.QRect(0, 40, 421, 41))
        self.label_zapis.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\';  border: 1px solid #8aeb46; color:white;background-color : #6ed427;\n"
"font-weight:900; }")
        self.label_zapis.setObjectName("label_zapis")
        Calculator.setCentralWidget(self.centralWidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_Ans.setText(_translate("Calculator", "Ans"))
        self.pushButton_decimal.setText(_translate("Calculator", "."))
        self.pushButton_plus.setText(_translate("Calculator", " + "))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_minus.setText(_translate("Calculator", " - "))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_mul.setText(_translate("Calculator", " x "))
        self.pushButton_powr.setText(_translate("Calculator", "^"))
        self.pushButton_factorial.setText(_translate("Calculator", "!"))
        self.pushButton_evaluate.setText(_translate("Calculator", "="))
        self.pushButton_zavorkaP.setText(_translate("Calculator", " ) "))
        self.pushButton_clean.setText(_translate("Calculator", "C"))
        self.pushButton_div.setText(_translate("Calculator", " / "))
        self.pushButton_zavorkaL.setText(_translate("Calculator", "("))
        self.pushButton_ln.setText(_translate("Calculator", "ln"))
        self.pushButton_root.setText(_translate("Calculator", "√"))
        self.pushButton_help.setStyleSheet(_translate("Calculator", "QPushButton { color:white;background-color: #44bb46; border: 1px solid white; font-weight:900;} \n"
"QPushButton:pressed { background-color:#348b35; } \n"
""))
        self.pushButton_help.setText(_translate("Calculator", "HELP"))
        self.label_zapis.setText(_translate("Calculator", ""))


