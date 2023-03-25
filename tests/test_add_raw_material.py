import pytest
import app
from confectionary import stockroom
from unittest.mock import patch, MagicMock


@patch('app.get_command', MagicMock(return_value="add shekar 10"))
def test_add_raw_material_to_stockroom_with_command():
    app.runner()
    assert 'shekar' in stockroom.RAW_MATERIALS and stockroom.RAW_MATERIALS['shekar'] == 10


@patch('app.get_command', MagicMock(return_value="add shekar 10"))
def test_if_the_raw_material_addition_was_successful_then_a_done_message_must_be_printed_on_the_output(capsys):
    label = "cms: "
    app.runner()
    out, err = capsys.readouterr()
    assert out == label + "Done\n"


@pytest.mark.parametrize('command',
                         [
                             "add",
                             "addhahg",
                             "add shekar",
                             "add shekar dd",
                             "add 44 43",
                             "add shekar -1",
                             "add shekar 1.5",
                             "add shekar 45 345",
                             "add shekar mekar 345",
                             "add.shekar.4",
                             "              ",
                             ""
                         ])
def test_if_the_wrong_add_command_is_entered_then_the_invalid_command_message_must_be_printed_on_the_output(capsys,
                                                                                                            command):
    label = "cms: "
    with patch('app.get_command', MagicMock(return_value=command)):
        app.runner()
        out, err = capsys.readouterr()
        assert out == label + "invalid command\n"


@patch('app.get_command', MagicMock(return_value="exit"))
def test_if_the_exit_command_is_entered_then_the_program_must_be_terminate():
    with pytest.raises(SystemExit) as e:
        app.main()
    assert e.value.code == 0


@pytest.fixture()
def add_multiple_raw_materials():
    q = 0
    for c in (10, 1, 2):
        with patch('app.get_command', MagicMock(return_value=f"add moraba {c}")):
            app.runner()
            q += c
    return q


def test_if_a_raw_material_is_added_twice_or_more_then_the_inventory_must_be_updated(add_multiple_raw_materials):
    quantity = add_multiple_raw_materials
    assert quantity == stockroom.RAW_MATERIALS["moraba"]