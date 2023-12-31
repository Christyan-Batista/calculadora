class FuncoesCalc:
    def __init__(self):
        self.mathexpression = ''
        self.currentoperation = None
        self.answer = None
        self.operations = ['*', '/', '+', '-', '(', ')']

    def data_info(self):
        self.expression = []
        temp = ''

        for num, c in enumerate(self.mathexpression):
            if c not in self.operations:
                temp += c
            else:
                if temp != '':
                    self.expression.append(float(temp))
                    temp = ''
                else:
                    pass
            if num == len(self.mathexpression) - 1 and temp != '':
                self.expression.append(float(temp))

    def percentage(self, finaleq, currenteq):
        temporary = ''
        if finaleq == '':
            temporary = str(float(currenteq) / 100)
            return temporary
        else:
            for char in finaleq:
                if char not in ['+', '-', '*', '/']:
                    temporary += char
            temporary = float(temporary) * float(currenteq) / 100
            if float(temporary) - int(temporary) != 0:
                return str(temporary)
            else:
                return str(int(temporary))

    def solve(self, mathexpression):
        self.mathexpression = mathexpression
        self.data_info()
        if len(self.expression) > 1:
            self.answer = eval(self.mathexpression)
            return str(self.answer)
        else:
            return None
