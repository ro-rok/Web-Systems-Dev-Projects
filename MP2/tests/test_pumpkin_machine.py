import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# add required test cases below

# rk868 10/21/2023 

# Test 1 - pumpkin must be the first selection
# I first checked that there is no pumpkin in progress, it should raise an exception if I choose a face stencil or extra
# Then I choose a pumpkin, and check that the pumpkin in progress is the one I chose

def test_pumpkin_selection_first(machine):
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Spooky Face")
        machine.handle_extra_choice("Dry Ice")
    machine.handle_pumpkin_choice("Medium Pumpkin")
    assert machine.inprogress_pumpkin[0].name == "Medium Pumpkin"



# rk868 10/21/2023
# Test 2 - can only add face stencils if they're in stock
# I first checked that the face stencil I want to choose is in stock, if it is, I use it until it's out of stock
# Then I choose a pumpkin, and check that the face stencil I want to choose is out of stock, it should raise an exception

def test_face_stencil_in_stock(machine):
    stencil = "Toothy Face"
    selected_stencil = next(ss for ss in machine.face_stencils if ss.name == stencil)
    while selected_stencil.in_stock():
        selected_stencil.use()
    machine.handle_pumpkin_choice("Medium Pumpkin")
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice(stencil)
    

# rk868 10/21/2023
# Test 3 - can only add extras if they're in stock
# I first checked that the extra I want to choose is in stock, if it is, I use it until it's out of stock
# Then I choose a pumpkin, and choose 'next' for face stencil to proceed to the extras stage
# Then I check that the extra I want to choose is out of stock, it should raise an exception

def test_extras_in_stock(machine):
    extra = "Spooky Sound Effects"
    selected_extra = next(se for se in machine.extras if se.name == extra)
    while selected_extra.in_stock():
        selected_extra.use()
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    with pytest.raises(OutOfStockException):
        machine.handle_extra_choice(extra)

# rk868 10/21/2023
# Test 4 - Can add up to 3 face stencils of any combination
# I selected a pumpkin, then I added 3 face stencils of any combination
# Then I tried to add a fourth face stencil which should raise an exception

def test_up_to_three_face_stencils(machine):
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")

# rk868 10/21/2023
# Test 5 - Can add up to 3 extras of any combination
# I selected a pumpkin, I selected 'next' for face stencil to proceed to the extras stage
# Then I added 3 extras of any combination
# Then I tried to add a fourth extra which should raise an exception

def test_up_to_three_extras(machine):
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Sticker Pack")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("Dry Ice")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Spooky Sound Effects")

# rk868 10/21/2023
# Test 6 - cost must be calculated properly based on the choices
# I used parametrize to test 3 different combinations of choices and their expected costs
# I chose a pumpkin, then I chose a face stencil, then I chose 'next' to proceed to the extras stage and chose an extra and 'done' to finish
# Then I calculated the cost and checked that it's equal to the expected cost
# I also checked that handling the payment with the calculated cost and the expected cost should not raise an exception

@pytest.mark.parametrize("pumpkin_choice, stencil_choice, extra_choice, expected_cost", 
                        [("Medium Pumpkin", "Happy Face", "Sticker Pack", 4.5),
                        ("Mini Pumpkin", "Scream Face", "Dry Ice", 2.25),
                        ("Large Pumpkin", "Toothy Face", "Spooky Sound Effects", 5.25)])
def test_cost_calculation(machine, pumpkin_choice, stencil_choice, extra_choice, expected_cost):
    machine.handle_pumpkin_choice(pumpkin_choice)
    machine.handle_face_stencil_choice(stencil_choice)
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice(extra_choice)
    machine.handle_extra_choice("done")
    calculated_cost = machine.calculate_cost()
    assert calculated_cost == expected_cost
    machine.handle_pay(calculated_cost, str(expected_cost))

# rk868 10/21/2023
# Test 7 - Total Sales (sum of costs) must be calculated properly
# I used parametrize to test 3 different combinations of choices and their expected total sales
# I chose a pumpkin, then I chose 2 face stencils, then I chose 'next' to proceed to the extras stage and chose 2 extras and 'done' to finish
# Then I calculated the total sales and checked that it's equal to the expected total sales
# I also checked that handling the payment with the calculated total sales and the expected total sales should not raise an exception


@pytest.mark.parametrize("pumpkin_choice, stencil_choice1, stencil_choice2, extra_choice1, extra_choice2, expected_total",
                        [("Medium Pumpkin", "Happy Face", "Scream Face", "Sticker Pack", "Dry Ice", 5.75),
                        ("Mini Pumpkin", "Toothy Face", "Happy Face", "Spooky Sound Effects", "Dry Ice", 4.5),
                        ("Large Pumpkin", "Scream Face", "Toothy Face", "Dry Ice", "Sticker Pack", 6.25)])
def test_total_sales(machine, pumpkin_choice, stencil_choice1, stencil_choice2, extra_choice1, extra_choice2, expected_total):
    machine.handle_pumpkin_choice(pumpkin_choice)
    machine.handle_face_stencil_choice(stencil_choice1)
    machine.handle_face_stencil_choice(stencil_choice2)
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice(extra_choice1)
    machine.handle_extra_choice(extra_choice2)
    machine.handle_extra_choice("done")
    assert expected_total == machine.calculate_cost()
    machine.handle_pay(expected_total, str(expected_total))
    calculated_total = machine.total_sales
    assert calculated_total == expected_total



# rk868 10/21/2023
# Test 8 - Total products variable should properly increment for each purchase
# I first checked that the total products is 0
# Then I chose a pumpkin, then I chose a face stencil, then I chose 'next' to proceed to the extras stage and chose an extra and 'done' to finish
# Then I calculated the cost and prepared it for the handle_pay method and simulated the payment
# Then I checked that the products total is incremented by 1

def test_total_products_increment(machine):
    initial_total_products = machine.total_products
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("done")
    calculated_cost = machine.calculate_cost()
    formatted_cost = str(calculated_cost)
    machine.handle_pay(calculated_cost, formatted_cost)
    assert machine.total_products == initial_total_products + 1
