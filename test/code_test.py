import pytest
from main import fileRead, printPrice


@pytest.fixture
def product_price():
    return {
        "Book": [
            ("03", 120),
            ("03", 100),
            ("03", 90),
            ("04", 80)
        ],
        "Chocolate": [
            ("03", 1000),
            ("04", 900),
            ("04", 850),
            ("04", 800)
        ],
        "Coffee": [
            ("03", 1500),
            ("04", 1400),
            ("04", 1350),
            ("04", 1300)
        ]
    }


@pytest.mark.parametrize("product, expected_output", [
    ("Book", {"03": -20}),
    ("Chocolate", {"04": -200}),
    ("Coffee", {"04": -200})])

def test_print_price(product_price, product, expected_output, capsys):
    printPrice({product: product_price[product]})
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    assert len(output_lines) == 1
    assert output_lines[0] == f"{list(expected_output.keys())[0]}: {list(expected_output.values())[0]}"


def test_file_read(product_price):
    filename = "test_products.txt"
    with open(filename, "w") as f:
        for product, prices in product_price.items():
            for price in prices:
                f.write(f"{product}, 2022-{price[0]}-{price[1]}\n")

    result = fileRead(filename)
    assert result == product_price
