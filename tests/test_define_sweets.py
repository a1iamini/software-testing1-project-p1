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


@pytest.mark.parametrize('command',
                         [
                          "define",
                          "definesweets",
                          "define sweetskhamei 3849: shekar 3, roghan 4",
                          "define sweets 5 3849: shekar 3, roghan 4",
                          "define sweets  3849: shekar 3, roghan 4",
                          "define sweets khamei : shekar 3, roghan 4",
                          "define sweets khamei: shekar 3, roghan 4",
                          "define sweets khamei 646:shekar 3, roghan 4",
                          "define sweets khamei 984: 87 3, roghan 4",
                          "define sweets khamei 894: 3, roghan 4",
                          "define sweets khamei 165: shekar nn, roghan 4",
                          "define sweets khamei 848: shekar, roghan 4",
                          "define sweets khamei 848: shekar  , roghan 4",
                          "define sweets khamei 848: shekar 3,roghan 4",
                          "define sweets khamei 848: shekar 3, 684 4",
                          "define sweets khamei 848: shekar 3, 4",
                          "define sweets khamei 848: shekar 3,  4",
                          "define sweets khamei 848: shekar 3, roghan jj",
                          "define sweets khamei 848: shekar 3, roghan",
                          "define sweets khamei 848: shekar 3, roghan -1",
                          "define sweets khamei 848: shekar 3, roghan 1.2",
                          "define sweets khamei 1.5: shekar 3, roghan 1",
                          "define sweets khamei -1: shekar 3, roghan 1",
                          "                                                 "
                         ])
def test_if_the_wrong_define_command_is_entered_then_the_invalid_command_message_must_be_printed_on_the_output(capsys,
                                                                                                               command):
    label = "cms: "
    with patch('app.get_command', MagicMock(return_value=command)):
        app.runner()
        out, err = capsys.readouterr()
        assert out == label + "invalid command\n"
