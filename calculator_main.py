import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 레이아웃 변경
        layout_buttons = QGridLayout()

        # 수식과 답을 위한 LineEdit 위젯 생성
        self.equation = QLineEdit("")
        self.equation.setReadOnly(True)  # 읽기 전용으로 설정

        # 버튼 생성
        button_numbers = [QPushButton(str(i)) for i in range(10)]
        button_dot = QPushButton(".")
        button_plus_minus = QPushButton("+/-")
        button_clear_entry = QPushButton("CE")
        button_clear_all = QPushButton("C")
        button_backspace = QPushButton("⌫")  # Backspace symbol
        button_equal = QPushButton("=")
        button_percent = QPushButton("%")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_square_root = QPushButton("x^(1/2)")
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_multi = QPushButton("x")
        button_divi = QPushButton("/")

        # 숫자 및 소수점 버튼의 위치 지정
        for i in range(1, 10):
            pass

        layout_buttons.addWidget(button_numbers[7], 2, 0)
        layout_buttons.addWidget(button_numbers[8], 2, 1)
        layout_buttons.addWidget(button_numbers[9], 2, 2)
        layout_buttons.addWidget(button_numbers[4], 3, 0)
        layout_buttons.addWidget(button_numbers[5], 3, 1)
        layout_buttons.addWidget(button_numbers[6], 3, 2)
        layout_buttons.addWidget(button_numbers[1], 4, 0)
        layout_buttons.addWidget(button_numbers[2], 4, 1)
        layout_buttons.addWidget(button_numbers[3], 4, 2)
        layout_buttons.addWidget(button_numbers[0], 5, 1)
        layout_buttons.addWidget(button_dot, 5, 2)
        layout_buttons.addWidget(button_plus_minus, 5, 0)

        # 연산자 버튼 추가 및 위치 조정
        layout_buttons.addWidget(button_plus, 4, 3)
        layout_buttons.addWidget(button_minus, 3, 3)
        layout_buttons.addWidget(button_multi, 2, 3)
        layout_buttons.addWidget(button_divi, 1, 3)

        # 나머지 버튼 추가
        layout_buttons.addWidget(button_clear_entry, 0, 1)
        layout_buttons.addWidget(button_backspace, 0, 3)
        layout_buttons.addWidget(button_clear_all, 0, 2)
        layout_buttons.addWidget(button_equal, 5, 3)  # rowspan=1, colspan=1
        layout_buttons.addWidget(button_percent, 0, 0)
        layout_buttons.addWidget(button_inverse, 1, 0)
        layout_buttons.addWidget(button_square, 1, 1)
        layout_buttons.addWidget(button_square_root, 1, 2)

        # 버튼 클릭 시그널 설정
        for i in range(10):
            button_numbers[i].clicked.connect(lambda state, num=i: self.number_button_clicked(num))

        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        button_plus_minus.clicked.connect(self.button_plus_minus_clicked)
        button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        button_clear_all.clicked.connect(self.button_clear_all_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_equal.clicked.connect(self.button_equal_clicked)
        button_percent.clicked.connect(self.button_percent_clicked)
        button_inverse.clicked.connect(self.button_inverse_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_square_root.clicked.connect(self.button_square_root_clicked)
        button_plus.clicked.connect(self.button_plus_clicked)
        button_minus.clicked.connect(self.button_minus_clicked)
        button_multi.clicked.connect(self.button_multi_clicked)
        button_divi.clicked.connect(self.button_divi_clicked)

        # 수식창을 layout에 추가
        main_layout.addWidget(self.equation)
        # 버튼 레이아웃 추가
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)
        self.show()

        #################
        ### functions ###
        #################

    def button_plus_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation += ' + '
        self.equation.setText(equation)

    def button_minus_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation += ' - '
        self.equation.setText(equation)

    def button_multi_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation += ' * '
        self.equation.setText(equation)

    def button_divi_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation += ' / '
        self.equation.setText(equation)

    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_clear_entry_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation = equation.rsplit(' ', 1)[0]
        self.equation.setText(equation)

    def button_clear_all_clicked(self):
        self.equation.setText("")

    def button_plus_minus_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            # 현재 수식의 마지막 문자가 숫자일 때만 부호를 변경합니다.
            if equation[0] == '-':
                equation = equation[1:]
            else:
                equation = '-' + equation
            self.equation.setText(equation)

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        try:
            solution = eval(equation)
            self.equation.setText(str(solution))
        except Exception as e:
            self.equation.setText("Error")

    def button_percent_clicked(self):
        equation = self.equation.text()
        if equation and equation[-1].isdigit():
            equation += ' % '
        self.equation.setText(equation)

    def button_inverse_clicked(self):
        equation = self.equation.text()
        try:
            result = 1 / eval(equation)
            self.equation.setText(str(result))
        except Exception as e:
            self.equation.setText("Error")

    def button_square_clicked(self):
        equation = self.equation.text()
        try:
            result = eval(equation) ** 2
            self.equation.setText(str(result))
        except Exception as e:
            self.equation.setText("Error")

    def button_square_root_clicked(self):
        equation = self.equation.text()
        try:
            result = eval(equation) ** 0.5
            self.equation.setText(str(result))
        except Exception as e:
            self.equation.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())