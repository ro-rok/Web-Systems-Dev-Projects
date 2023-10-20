from enum import Enum
import sys
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from PumpkinMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Pumpkin(Usable):
    pass


class FaceStencil(Usable):
    pass


class Extra(Usable):
    pass


class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4


class PumpkinMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3
    def __init__(self):
        self.pumpkins = [Pumpkin(name="Mini Pumpkin", cost=1),
                    Pumpkin(name="Small Pumpkin", cost=2),
                    Pumpkin(name="Medium Pumpkin", cost=2.5),
                    Pumpkin(name="Large Pumpkin", cost=3)]
        self.face_stencils = [FaceStencil(name="Happy Face", quantity=10, cost=1),
                        FaceStencil(name="Scream Face", quantity=10, cost=1),
                        FaceStencil(name="Toothy Face", quantity=10, cost=1),
                        FaceStencil(name="Spooky Face", quantity=10, cost=1)]
        self.extras = [Extra(name="Small Candle", quantity=10, cost=.25),
                Extra(name="LED Candle", quantity=10, cost=.25),
                Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
                Extra(name="Sticker Pack", quantity=10, cost=1.00),
                Extra(name="Paint Kit", quantity=10, cost=3),
                Extra(name="Dry Ice", quantity=10, cost=.25),
                Extra(name="Googly Eyes", quantity=10, cost=.25),
                Extra(name="Glitter", quantity=10, cost=.25)]

        # variables
        self.remaining_uses = PumpkinMachine.USES_UNTIL_CLEANING
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0

        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    # rules
    # 1 - pumpkin must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - face stencils can't exceed max
    # 4 - extras can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more things can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_products should increment properly after a payment

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        """Called when a pumpkin is complete"""
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, _pumpkin):
        self.pick_pumpkin(_pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, _face_stencil):
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(_face_stencil)

    def handle_extra_choice(self, _extra):
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(_extra)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += expected  # <-- TODO increment only if successful
            # print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_pumpkin(self):
        print(
            f"Current Pumpkin: {','.join([x.name for x in self.inprogress_pumpkin])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_pumpkin
        
        # rk868 10/20/2023
        # If length of inprogress_pumpkin is 0, return 0 as there is no pumpkin in progress to calculate cost for 
        # If length of inprogress_pumpkin is not 0, iterate through the list and add the cost of each item to the total
        # Return the total

        if len(self.inprogress_pumpkin) == 0:
            return 0
        total = 0
        for item in self.inprogress_pumpkin:
            total += item.cost
        return total
    


    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.pumpkins))))}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"What type of face stencil would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.face_stencils))))}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.extras))))}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # TODO show expected value as currency format
                # TODO require total to be entered as currency format
                total = input(
                    f"Your total is ${expected:,.2f}, please enter the exact value.\n")
                if total == "quit":
                    print("Quitting the pumpkin machine")
                    return 1
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    # exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the pumpkin machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the pumpkin machine")
            sys.exit()
        # TODO items below
        # Note: Stage/category refers to the enum towards the top. Make sure error messages are very clear to the user
        # handle OutOfStockException
            # show an appropriate message of what stage/category was out of stock
        
        # rk868 10/20/2023 
        # If the exception is OutOfStockException, print the message 
        # "Sorry, the choice in {self.currently_selecting.name} is out of stock."
        except OutOfStockException as e:
            print(f"Sorry, the choice in {self.currently_selecting.name} is out of stock.")


        # handle NeedsCleaningException
            # prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            # print a message whether or not the machine was cleaned
        
        # rk868 10/20/2023
        # If the exception is NeedsCleaningException, prompt the user to type "clean" to trigger clean_machine()
        # If the user types "clean", clean the machine and print "Machine has been cleaned."
        # If the user types anything else, print "Ignoring input. Machine not cleaned."

        except NeedsCleaningException as e:
            clean_command = input("The machine needs cleaning. Type 'clean' to clean it: ")
            if clean_command.lower() == 'clean':
                self.clean_machine()
                print("Machine has been cleaned.")
            else:
                print("Ignoring input. Machine not cleaned.")


        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid choice was in

        # rk868 10/20/2023
        # If the exception is InvalidChoiceException, print the message
        # "Sorry, the choice in {self.currently_selecting.name} is invalid. Please choose again."

        except InvalidChoiceException as e:
            print(f"Sorry, the choice in {self.currently_selecting.name} is invalid. Please choose again.") 

        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category

        # rk868 10/20/2023
        # If the exception is ExceededRemainingChoicesException, print the message
        # "Sorry, you have exceeded the number of choices in {self.currently_selecting.name}."
        # If the current stage/category is Pumpkin, move to FaceStencil
        # If the current stage/category is FaceStencil, move to Extra
        # If the current stage/category is Extra, move to Pay

        except ExceededRemainingChoicesException as e:
            print(f"Sorry, you have exceeded the number of choices in {self.currently_selecting.name}.")
            
            if self.currently_selecting == STAGE.Pumpkin:
                self.currently_selecting = STAGE.FaceStencil
            elif self.currently_selecting == STAGE.FaceStencil:
                self.currently_selecting = STAGE.Extra
            elif self.currently_selecting == STAGE.Extra:
                self.currently_selecting = STAGE.Pay
        
        # handle InvalidPaymentException
            # show an appropriate message
        
        # rk868 10/20/2023
        # If the exception is InvalidPaymentException, print the message
        # "Sorry, the payment is invalid. Please try again with the exact amount."

        except InvalidPaymentException as e:
            print("Sorry, the payment is invalid. Please try again with the exact amount.")

        except Exception as e:
            # this is a default catch all, follow the steps above
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()


if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()