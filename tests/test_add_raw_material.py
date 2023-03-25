import app
from confectionary import stockroom
from unittest.mock import patch, MagicMock


@patch('app.get_command', MagicMock(return_value="add shekar 10"))
def test_add_raw_material_to_stockroom_with_command():
    app.runner()
    assert 'shekar' in stockroom.RAW_MATERIALS and stockroom.RAW_MATERIALS['shekar'] == 10

