class MyCalc:
    def __init__(self):
        self.ans = 0   

    #rk868 15/10/2023 : Added static methods to check if a string is a number
    @staticmethod
    def _is_float(val):
        try:
            val = float(val)
            return True
        except:
            return False

    @staticmethod
    def _is_int(val):
        try:
            val = int(val)
            return True
        except:
            return False

    @staticmethod
    def _as_number(val):
        if MyCalc._is_float(val):
            return float(val)
        elif MyCalc._is_int(val):
            return int(val)
        else:
            raise Exception("Not a number")
        
    
    def calc(self, num1, num2, operator):
        # rk868 15/10/2023 : if input equation has ans, then use the previous answer 
        if num1 == "ans":
            return self.calc(self.ans, num2, operator)
        elif num2 == "ans":
            return self.calc(num1, self.ans, operator)
        
        # rk868 15/10/2023 : Convert the input strings to numbers
        num1 = MyCalc._as_number(num1)
        num2 = MyCalc._as_number(num2)

        # rk868 15/10/2023: Storing the sum in the instance variable 'ans' 
        if operator == "+":
            self.ans = num1+num2
        # rk868 15/10/2023: Storing the difference in the instance variable 'ans'
        elif operator == "-":
            self.ans = num1-num2
        # rk868 15/10/2023: Storing the product in the instance variable 'ans'
        elif operator == "*":
            self.ans = num1*num2
        # rk868 15/10/2023: Storing the quotient in the instance variable 'ans' and handling division by zero error     
        elif operator == "/":
            try:
                self.ans = num1/num2
            except:
                print("Error: Division by zero")
        # rk868 15/10/2023: Handling invalid operator error
        else:
            print("Error: Unknown operator")
        return self.ans
    
    def main(self):
        # rk868 15/10/2023: main function to take input from user and display the result
        is_running = True
        iSTR = input("Are you ready?")
        if iSTR in ["yes", "y", "Y", "YES", "Yes"]:
            while is_running:
                iSTR = input("What is your eq:")
                if iSTR in ["exit", "quit", "q", "Q"]:
                    is_running = False
                else:
                    print("Your eq was :" + str(iSTR))
                    operators = ["+", "/", "*","-"]
                    for operator in operators:
                        if operator in iSTR:
                            nums = iSTR.split(operator)
                            r = self.calc(nums[0].strip(), nums[1].strip(), operator)
                            print("The result is :" + str(r))
        else:
            print("Good bye")
            is_running = False

if __name__ == "__main__":
    calc = MyCalc()
    calc.main()
    print(f"The final answer is {calc.ans}")
