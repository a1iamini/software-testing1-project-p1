import pytest

import app
from unittest.mock import patch, MagicMock
from confectionary import store
from confectionary import workshop


def test_if_sweets_is_defined_then_its_name_and_price_must_be_added_to_the_store():
    with patch('app.get_command', MagicMock(return_value="define sweets khamei 10000: khame 10, shekar 5")):
        app.runner()
        assert "khamei" in store.SWEETS and store.SWEETS["khamei"] == 10000


@patch('app.get_command', MagicMock(return_value="define sweets khamei 10000: khame 10, shekar 5"))
def test_if_the_sweets_definition_was_successful_then_a_done_message_must_be_printed_on_the_output(capsys):
    label = "cms: "
    app.runner()
    out, err = capsys.readouterr()
    assert out == label + "Done\n"


def test_if_sweets_is_defined_then_its_raw_material_specification_must_be_added_to_the_workshop():
    with patch('app.get_command', MagicMock(return_value="define sweets khamei 10000: khame 10, shekar 5")):
        app.runner()
        assert 'khamei' in workshop.SWEETS_SPEC \
               and workshop.SWEETS_SPEC['khamei']['khame'] == 10 \
               and workshop.SWEETS_SPEC['khamei']['shekar'] == 5


@pytest.fixture()
def define_more():
    commands = [
        "define sweets khamei 20000: khame 10, shekar 5",
        "define sweets khamei 10000: khame 12",
        "define sweets khamei 30000: khame 10, shekar 5",
        "define sweets khamei 70000: khame 3, ghand 3",
    ]
    for c in commands:
        with patch('app.get_command', MagicMock(return_value=c)):
            app.runner()


def test_if_sweets_is_defined_for_second_or_more_times_then_the_last_definition_should_be_considered(define_more):
    assert 'khamei' in workshop.SWEETS_SPEC \
           and workshop.SWEETS_SPEC['khamei']['khame'] == 3 \
           and workshop.SWEETS_SPEC['khamei']['ghand'] == 3 \
           and "shekar" not in workshop.SWEETS_SPEC['khamei'] \
           and "khamei" in store.SWEETS \
           and store.SWEETS["khamei"] == 70000
