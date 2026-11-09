import pytest
from app.reservation import Stock, Reservation


@pytest.fixture
def stock():
    return Stock(5)


def test_reservation_de_deux_unites_confirmee(stock):
    reservation = Reservation(stock)
    assert reservation.reserver(2) == "confirmee"
    assert stock.quantite == 3


def test_reservation_superieure_au_stock_refusee(stock):
    reservation = Reservation(stock)
    assert reservation.reserver(6) == "refusee"
    assert stock.quantite == 5


def test_reservation_de_tout_le_stock(stock):
    reservation = Reservation(stock)
    assert reservation.reserver(5) == "confirmee"
    assert stock.quantite == 0


def test_quantite_nulle_declenche_value_error_sans_modifier_stock(stock):
    reservation = Reservation(stock)
    with pytest.raises(ValueError):
        reservation.reserver(0)
    assert stock.quantite == 5
