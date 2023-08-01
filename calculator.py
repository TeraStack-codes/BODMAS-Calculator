class Calculator:
    def __init__(self, text):
        self.maintext = text
        self.list = []

    def start(self):
        self.list = self.tokenize(self.maintext)
        self.list = self.removeBrackets(self.list)
        self.list = self.evaluate(self.list)
        print(f'End of Processing: {self.list}')

    def tokenize(self, text):
        operators = ['+', '-', '*', '/', '^', '(', ')']
        tokens = []
        current_number = ""

        for char in text:
            if char.isdigit() or char == '.':
                current_number += char
            elif char in operators:
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                tokens.append(char)

        if current_number:
            tokens.append(current_number)

        return tokens

    def removeBrackets(self, inputList):
        stack = []
        result = []

        for char in inputList:
            if char == '(':
                stack.append(result)
                result = []
            elif char == ')':
                if stack:
                    prev_result = stack.pop()
                    prev_result.append(result)
                    result = prev_result
            else:
                result.append(char)

        return result

    def evaluate(self, expression):
        if isinstance(expression, list):
            if len(expression) == 3:
                operand1 = self.evaluate(expression[0])
                operator = expression[1]
                operand2 = self.evaluate(expression[2])

                if operator == '+':
                    return operand1 + operand2
                elif operator == '-':
                    return operand1 - operand2
                elif operator == '*':
                    return operand1 * operand2
                elif operator == '/':
                    return operand1 / operand2
                elif operator == '^':
                    return operand1 ** operand2
                else:
                    print("Invalid operator!")
                    return None
            else:
                return self.evaluate(expression[0])
        else:
            return float(expression)


Calc = Calculator('(3846*3846) + (394374*394374) + 2*(3846*394374)')
Calc.start()
