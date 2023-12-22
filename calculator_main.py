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

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())