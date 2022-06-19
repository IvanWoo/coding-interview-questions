import pytest
from puzzles.search_suggestions_system import suggested_products


@pytest.mark.parametrize(
    "products, search_term, expected",
    [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
            ],
        ),
        (
            ["bags", "baggage", "banner", "box", "cloths"],
            "bags",
            [
                ["baggage", "bags", "banner"],
                ["baggage", "bags", "banner"],
                ["baggage", "bags"],
                ["bags"],
            ],
        ),
        (["havana"], "tatiana", [[], [], [], [], [], [], []]),
    ],
)
def test_suggested_products(products, search_term, expected):
    assert suggested_products(products, search_term) == expected
