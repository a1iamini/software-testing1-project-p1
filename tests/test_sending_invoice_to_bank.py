import pytest

import app
from unittest.mock import MagicMock, patch


@pytest.fixture
def prerequisites():
    commands = ['add khame 60',
                'add shekar 25',
                'define sweets khamei 10000: khame 10, shekar 5']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()


@patch('app.get_command', MagicMock(return_value="customer buy khamei 3"))
def test_if_purchase_is_successful_then_the_function_of_sending_the_report_to_bank_must_be_called_once(prerequisites):
    with patch('commands.send_report_to_bank', MagicMock()) as m:
        app.runner()
    m.assert_called_once()
