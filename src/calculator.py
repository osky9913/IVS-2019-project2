from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow,Ui_Calculator):
      def __init__(self):
          super().__init__()
          self.setupUi(self)
          self.show()
          self.pushButton_0.clicked.connect(self.digit_pressed)
          self.pushButton_1.clicked.connect(self.digit_pressed)
          self.pushButton_2.clicked.connect(self.digit_pressed)
          self.pushButton_3.clicked.connect(self.digit_pressed)
          self.pushButton_4.clicked.connect(self.digit_pressed)
          self.pushButton_5.clicked.connect(self.digit_pressed)
          self.pushButton_6.clicked.connect(self.digit_pressed)
          self.pushButton_7.clicked.connect(self.digit_pressed)
          self.pushButton_8.clicked.connect(self.digit_pressed)
          self.pushButton_9.clicked.connect(self.digit_pressed)

          self.pushButton_decimal.clicked.connect(self.decimal_pressed)
          self.pushButton_plus.clicked.connect(self.plus_pressed)
          self.pushButton_minus.clicked.connect(self.minus_pressed)
          self.pushButton_mul.clicked.connect(self.mul_pressed)
          self.pushButton_powr.clicked.connect(self.powr_pressed)
          self.pushButton_factorial.clicked.connect(self.factorial_pressed)
          self.pushButton_div.clicked.connect(self.div_pressed)
          self.pushButton_bracketL.clicked.connect(self.bracketL_pressed)
          self.pushButton_bracketP.clicked.connect(self.bracketP_pressed)
          self.pushButton_ln.clicked.connect(self.ln_pressed)
          self.pushButton_root.clicked.connect(self.root_pressed)

          self.pushButton_clean.clicked.connect(self.clean_pressed)


      def digit_pressed(self):
          button = self.sender()
          self.label_write.setText(self.label_write.text() + button.text())

      def  decimal_pressed(self):
          self.label_write.setText(self.label_write.text() + '.')

      def  plus_pressed(self):
          self.label_write.setText(self.label_write.text() + " " + '+' + " ")

      def  minus_pressed(self):
          self.label_write.setText(self.label_write.text() + " " + '-' + " ")

      def  powr_pressed(self):
          self.label_write.setText(self.label_write.text() + '^')

      def  ln_pressed(self):
          self.label_write.setText(self.label_write.text() + 'ln')

      def  mul_pressed(self):
          self.label_write.setText(self.label_write.text() + " " + 'x' + " ")

      def  bracketL_pressed(self):
          self.label_write.setText(self.label_write.text() + '(')

      def  bracketP_pressed(self):
          self.label_write.setText(self.label_write.text() + ')')

      def  div_pressed(self):
          self.label_write.setText(self.label_write.text() + " " + '/' + " ")

      def  root_pressed(self):
          self.label_write.setText(self.label_write.text() + '√')

      def factorial_pressed(self):
          self.label_write.setText(self.label_write.text() + '!')

      def clean_pressed(self):
          self.label_write.setText("")
