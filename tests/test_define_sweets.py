import app
from unittest.mock import patch, MagicMock
from confectionary import store


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
