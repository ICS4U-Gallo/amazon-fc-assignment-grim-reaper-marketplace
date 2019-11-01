from functions import *

# first test
one = Trolly()
two = Trolly()

# second and fourth test
a = Product('a', 1, 1)
b = Product('b', 51, 2)
c = Product('c', 51, 10)

# third test
box = Shipment('Box', Product.incoming_products)

def test_create_trolly():
    assert one.weight_capacity == 100
    assert one.storage == []
    assert one.id == 0
    assert two.id == 1


def test_create_product():
    result = [a.name, a.weight, a.barcode]
    expected = ['a', 1, 1]
    assert result == expected
    assert len(Product.incoming_products) == 3


def test_create_shipment():
    assert box.products[0].name == 'a'
    assert box.products[1].name == 'b'


def test_move_to_trolly():
    box.load_to_trolly()
    assert len(box.products) == 0
    assert one.storage[0].name == 'a' and one.storage[1].name == 'b'
    assert two.storage[0].name == 'c'


def test_calculate_weight():
    result = one.calculate_weight()
    expected = a.weight + b.weight
    assert result == expected

    result = two.calculate_weight()
    expected = 51
    assert result == expected


def test_reset():
    Product.incoming_products = ['walter']
    Trolly.all_trollies = ['walter']
    num_trolly = 5
    reset()
    assert Product.incoming_products == []
    assert Trolly.all_trollies == []
    assert Trolly.num_trolly == 0