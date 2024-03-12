def test_sort(func):
    print("func doing ->")
    print(func.__doc__)
    source = "papa"
    ans = "apap"
    print(f"test1\n--------\n test_date = {source}, waited answer = {ans}\n------")
    assert func(source) == ans


def reverse_string(str: str):
    """func to reverse string"""
    return str[::-1]


test_sort(reverse_string)
