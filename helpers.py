from data import *
from unittest.mock import Mock


def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BUN_NAME
    return mock_bun


def receipt_():
    receipt = [f'(==== {BUN_NAME} ====)']
    receipt.append(f'= {str(FILLING_TYPE).lower()} {FILLING_NAME} =')
    receipt.append(f'(==== {BUN_NAME} ====)\n')
    receipt.append(f'Price: {300.}')
    return '\n'.join(receipt)
