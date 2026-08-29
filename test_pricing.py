import pytest

from pricing import discounted_cents


def test_discount_rounds_half_cent_away_from_zero():
    assert discounted_cents(105, 50) == 53


def test_discount_boundaries():
    assert discounted_cents(999, 0) == 999
    assert discounted_cents(999, 100) == 0


def test_invalid_values_are_rejected():
    with pytest.raises(ValueError):
        discounted_cents(-1, 10)
    with pytest.raises(ValueError):
        discounted_cents(100, 101)
