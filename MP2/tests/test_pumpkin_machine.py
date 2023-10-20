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

# sample fixture, can delete if not using


@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

# sample fixture, can delete if not using


@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    # machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using


def test_production_line(second_order):
    for j in second_order.pumpkins:
        print(second_order.inprogress_pumpkin)
        if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
            print(f"Pumkin {j.name.lower()} matches in progress \
                {second_order.inprogress_pumpkin[0].name.lower()}")
            assert True
            return

    assert False

# add required test cases below
