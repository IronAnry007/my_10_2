import pytest

from src.calculate_taxes import calculate_tax


@pytest.mark.parametrize("price, tax_rate, expected", [(100, 10, 110),
                                                       (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(-1, 10)


def test_calculate_tax_invalid_tax_rate_below_zero():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)


def test_calculate_tax_invalid_tax_rate():
    with pytest.raises(ValueError):
        calculate_tax(100, 100)


@pytest.mark.parametrize("price, tax_rate, discount, expected", [(100, 10, 0, 110.0),
                                                                 (100, 10, 10, 99.0),
                                                                 (100, 10, 100, 0.0)])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected


def test_calculate_tax_no_discount():
    assert calculate_tax(price=100, tax_rate=10) == 110


@pytest.mark.parametrize("round_digits, expected", [(0, 99),
                                                    (1, 99.4),
                                                    (2, 99.42),
                                                    (3, 99.425)])
def test_calculate_tax_round(round_digits, expected):
    assert  calculate_tax(100, 2.5, discount=3, round_digits=round_digits) == expected


@pytest.mark.parametrize("price, tax_rate, discount, round_digits", [("100", 10, 0, 1),
                                                                               (100, "10", 10, 1),
                                                                               (100, 10, "100", 1),
                                                                               (100, 10, 100, "1")])
def test_calculate_tax_wrong_type(price, tax_rate, discount, round_digits):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_digits=round_digits)


def test_calculate_tax_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 3, 3, 1)
