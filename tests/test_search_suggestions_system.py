from puzzles.search_suggestions_system import suggested_products


def test_suggested_products():
    assert suggested_products(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
    ) == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]

    assert suggested_products(["havana"], "havana") == [
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
    ]

    assert suggested_products(
        ["bags", "baggage", "banner", "box", "cloths"], "bags"
    ) == [
        ["baggage", "bags", "banner"],
        ["baggage", "bags", "banner"],
        ["baggage", "bags"],
        ["bags"],
    ]

    assert suggested_products(["havana"], "tatiana") == [[], [], [], [], [], [], []]
