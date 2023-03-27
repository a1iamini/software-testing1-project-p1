import app
import pytest
from unittest.mock import patch, MagicMock
from confectionary import store, stockroom, workshop


@pytest.fixture()
def add(request):
    commands = ['add nabat 60', 'add asal 25', 'add khame 2', 'add shekar 1']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()

    def cleanup():
        stockroom.RAW_MATERIALS = dict()

    request.addfinalizer(cleanup)


@pytest.fixture()
def define(request):
    commands = ['define sweets nabatasali 10000: nabat 10, asal 5',
                'define sweets khamei 10000: khame 3, shekar 1']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()

    def cleanup():
        store.CASH_DESK = 0
        store.SWEETS = dict()
        workshop.SWEETS_SPEC = dict()

    request.addfinalizer(cleanup)


@patch('app.get_command', MagicMock(return_value='customer buy nabatasali 3'))
def test_if_the_purchase_of_sweets_is_successful_then_the_purchase_amount_must_be_added_to_cash_desk(define, add):
    app.runner()
    assert store.CASH_DESK == 30000


@patch('app.get_command', MagicMock(return_value='customer buy nabatasali 1'))
def test_if_raw_materials_have_been_used_to_bake_sweets_then_the_inventory_should_be_reduced(define, add):
    app.runner()
    assert stockroom.RAW_MATERIALS['nabat'] == 50 and stockroom.RAW_MATERIALS['asal'] == 20


@patch('app.get_command', MagicMock(return_value='customer buy nabatasali 1'))
def test_if_the_buy_sweets_was_successful_then_a_done_message_must_be_printed_on_the_output(capsys):
    with patch('app.buy'):
        label = "cms: "
        app.runner()
        out, err = capsys.readouterr()
        assert out == label + "Done\n"


@patch('app.get_command', MagicMock(return_value='customer buy khamei 1'))
def test_if_the_raw_materials_are_low_or_less_then_1_sweets_then_an_appropriate_message_should_be_printed(capsys, add,
                                                                                                          define):
    label = "cms: "
    app.runner()
    out, err = capsys.readouterr()
    assert out[-27:] == label + "Insufficient material\n"


@pytest.mark.parametrize('command',
                         [
                             "customer",
                             "customerbuy",
                             "customer buynabatasali 1",
                             "customer buy 8 1",
                             "customer buy -1 1",
                             "customer buy  1",
                             "customer buy nabatasali1",
                             "customer buy nabatasali -1",
                             "customer buy nabatasali 1.5",
                             "customer buy nabatasali nbv",
                             "customer buy nabatasali  ",
                             "                            "
                         ])
def test_if_the_wrong_buy_command_is_entered_then_the_invalid_command_message_must_be_printed_on_the_output(capsys,
                                                                                                            add,
                                                                                                            define,
                                                                                                            command):
    label = "cms: "
    with patch('app.get_command', MagicMock(return_value=command)):
        app.runner()
        out, err = capsys.readouterr()
        assert out[-21:] == label + "invalid command\n"
