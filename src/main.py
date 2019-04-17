#!/usr/bin/python3

##
# @file main.py
# @author xsvobo1t
# @brief This is the main program to run the Calculator

import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
