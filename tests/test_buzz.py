from fizzbuzz import fizzbuzz

expected = {
    "data": [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
        "16",
        "17",
        "fizz",
        "19",
        "buzz",
    ]
}

def test_fizzbuzz():
    assert fizzbuzz(20) == expected
