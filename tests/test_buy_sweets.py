import app
import pytest
from unittest.mock import patch, MagicMock
from confectionary import store, stockroom, workshop


@pytest.fixture()
def add(request):
    commands = ['add nabat 60', 'add asal 25']
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()

    def cleanup():
        stockroom.RAW_MATERIALS = dict()

    request.addfinalizer(cleanup)


@pytest.fixture()
def define(request):
    commands = ['define sweets nabatasali 10000: nabat 10, asal 5']
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
