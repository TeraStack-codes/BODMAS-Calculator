class Calculator:
    def __init__(self,text):
        self.maintext = text
        
    def start(self):
        print(self.joinNumbers(self.maintext))
        self.removeBrackets(self.maintext)

    def joinNumbers(self,text):
        prevNumberIsInt = [False,False]
        currentNumberIsInt = [False,False]
        wholeList = []
        for part in text:
            try:
                int(part)
                currentNumberIsInt[0] = True
                currentNumberIsInt[1] = part
            except ValueError:
                wholeList.append(part)
                currentNumberIsInt[0] = False
                currentNumberIsInt[1] = False
                

            if currentNumberIsInt[0] == True and prevNumberIsInt[0] == True:
                newPart = prevNumberIsInt[1] + currentNumberIsInt[1]
                wholeList.append(newPart)
                z = []
                for x,y in enumerate(wholeList):
                    if y != prevNumberIsInt[1]:
                        pass
                    else:
                        z.append(x)
                try:
                    a = max(z)
                except ValueError:
                    pass
                else:
                    print(f'Just Poped: {wholeList[a]}')
                    wholeList.pop(a)
                    
            elif currentNumberIsInt[0] == True:
                wholeList.append(part)
            
            prevNumberIsInt[0] = currentNumberIsInt[0]
            prevNumberIsInt[1] = currentNumberIsInt[1]
        
        return wholeList

    
    def removeBrackets(self,text):
        # todo PROCESS ALL THE BRACKETS
        pass

Calc = Calculator('(2+24)/(20*50)')
Calc.start()