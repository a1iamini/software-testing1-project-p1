import app
import pytest
from unittest.mock import patch, MagicMock
from confectionary import store


@pytest.fixture()
def add_raw_materials():
    commands = ['add khame 60', 'add shekar 25']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()


@pytest.fixture()
def define_sweets():
    commands = ['define sweets khamei 10000: khame 10, shekar 5']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()


@patch('app.get_command', MagicMock(return_value='customer buy khamei 3'))
def test_if_the_purchase_of_sweets_is_successful_then_the_purchase_amount_must_be_added_to_cash_desk(define_sweets,
                                                                                                     add_raw_materials):
    app.runner()
    assert store.CASH_DESK == 30000

