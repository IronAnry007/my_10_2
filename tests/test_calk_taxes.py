import pytest
from src.calculate_taxes import calculate_taxes

@pytest.fixture
def prices():
    # Возвращаем список цен
    return [1000.0, 800.0,  500.0]


@pytest.mark.parametrize("tax_rate, expected", [(5, [1050, 840, 525]),
                                                (10, [1100, 880, 550]),
                                                (15, [1150, 920, 575])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], tax_rate=10)
