from customtkinter import *
from funcoescalc import *
from tkinter import *

class App:
    def __init__(self):
        self.calctool = None
        self.window = CTk()
        self.window.iconbitmap(r'images/calculator.ico')

        self.window_config()
        self.math_expression = StringVar(value='0')
        self.final_math_expression = StringVar(value='')
        self.result = ''
        self.ans = 0
        self.operation_done = False
        self.frames()
        self.botoes()
        self.visor_expression()
        self.window.mainloop()

    def window_config(self):
        self.window.configure(fg_color='#1C1C1C')
        self.window.geometry('360x575')
        self.window.title('Calculadora')
        self.window.resizable(False, False)

    def frames(self):
        self.visor = CTkFrame(self.window)
        self.visor.configure(fg_color='#1C1C1C')
        self.visor.place(relheight=0.25, relwidth=1)

        self.frame_button = CTkFrame(self.window)
        self.frame_button.configure(fg_color='#1C1C1C')
        self.frame_button.place(rely=0.25, relheight=0.75, relwidth=1)

    def botoes(self):
        cont = 0
        color = ''
        self.numbers = [
                            CTkButton(self.frame_button, text='AC ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.clear_screen()),
                            CTkButton(self.frame_button, text='+/-', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=self.moreless),
                            CTkButton(self.frame_button, text=' % ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=self.percentagefunc),
                            CTkButton(self.frame_button, text=' / ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.math_operation('/')),
                            CTkButton(self.frame_button, text=' 7 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('7')),
                            CTkButton(self.frame_button, text=' 8 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('8')),
                            CTkButton(self.frame_button, text=' 9 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('9')),
                            CTkButton(self.frame_button, text=' X ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.math_operation('*')),
                            CTkButton(self.frame_button, text=' 4 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('4')),
                            CTkButton(self.frame_button, text=' 5 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('5')),
                            CTkButton(self.frame_button, text=' 6 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('6')),
                            CTkButton(self.frame_button, text=' - ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.math_operation('-')),
                            CTkButton(self.frame_button, text=' 1 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('1')),
                            CTkButton(self.frame_button, text=' 2 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('2')),
                            CTkButton(self.frame_button, text=' 3 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('3')),
                            CTkButton(self.frame_button, text=' + ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.math_operation('+'))
                        ]
        for r in range(0, 4, 1):
            for c in range(0, 4, 1):
                if r == 0 and c < 3:
                    color = '#D4D4D2'
                if r > 0 and c < 3:
                    color = '#505050'
                if c == 3:
                    color = '#FF9500'

                self.numbers[cont].configure(width=30, height=75, corner_radius=25, fg_color=color)
                self.numbers[cont].grid(row=r, column=c, padx=5, pady=5)
                cont += 1

        self.last_row_buttons = [
                                    CTkButton(self.frame_button, text=' 0 ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('0')),
                                    CTkButton(self.frame_button, text=' . ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.update_visor('.')),
                                    CTkButton(self.frame_button, text=' = ', text_color='white', fg_color='#505050', font=('Helvetica', 20), command=lambda: self.math_operation('='))
                                ]

        self.last_row_buttons[0].configure(width=60, height=75, corner_radius=70)
        self.last_row_buttons[0].place(rely=0.805, relx=0.02)
        self.last_row_buttons[1].configure(width=30, height=75, corner_radius=25)
        self.last_row_buttons[1].grid(row=4, column=2, padx=5, pady=5)
        self.last_row_buttons[2].configure(width=30, height=75, corner_radius=25, fg_color='#FF9500')
        self.last_row_buttons[2].grid(row=4, column=3, padx=5, pady=5)

    def visor_expression(self):
        self.text_visor_size = 50
        self.visor_equation = CTkLabel(self.visor, textvariable=self.math_expression, font=('Helvetica', self.text_visor_size, 'bold'),
                                       text_color='white')
        self.visor_equation.place(relx=0.05, rely=0.5)

        self.view_expression = CTkLabel(self.visor, textvariable=self.final_math_expression, font=('Helvetica', 20, 'bold'),
                                       text_color='#D4D4D2')
        self.view_expression.place(relx=0.05, rely=0.05)


    def update_visor(self, number):

        if self.math_expression.get() == '0' or self.operation_done:
            self.math_expression.set('')
            self.operation_done = False

        if len(self.math_expression.get()) < 9:
            self.math_expression.set(str(self.math_expression.get())+ str(number))
        elif len(self.math_expression.get()) == 20:
            return
        else:
            if self.text_visor_size > 30:
                self.text_visor_size -= 5
                self.visor_equation.configure(font=('Helvetica', self.text_visor_size, 'bold'))
                self.math_expression.set(str(self.math_expression.get()) + str(number))
            else:
                self.text_visor_size = 30
                self.visor_equation.configure(font=('Helvetica', self.text_visor_size, 'bold'))
                self.math_expression.set(str(self.math_expression.get()) + str(number))

    def clear_screen(self):
        self.math_expression.set('0')
        self.final_math_expression.set('')

    def math_operation(self, mathsymbol):
        answer = None
        self.calctool = FuncoesCalc()

        if len(self.final_math_expression.get()) > 0 and self.operation_done is not False:
            if self.final_math_expression.get()[-1] in ['*', '/'] and mathsymbol in ['+', '-']:
                self.math_expression.set('-')
                self.operation_done = False
                return

        answer = self.calctool.solve(self.final_math_expression.get() + self.math_expression.get())

        if answer is not None:
            self.operation_done = True
            self.math_expression.set(answer)
            if mathsymbol == '=':
                self.final_math_expression.set('')
            else:
                self.final_math_expression.set(answer + mathsymbol)
                self.math_expression.set('0')
        else:
            self.final_math_expression.set(self.math_expression.get() + mathsymbol)
            self.math_expression.set('0')

    def percentagefunc(self):
        self.calctool = FuncoesCalc()
        self.math_expression.set(self.calctool.percentage(self.final_math_expression.get(), self.math_expression.get()))

    def moreless(self):
        if float(self.math_expression.get()) - int(self.math_expression.get()) != 0:
            self.math_expression.set(str(float(self.math_expression.get())*(-1)))
        else:
            self.math_expression.set(str(int(self.math_expression.get()) * (-1)))

App()
