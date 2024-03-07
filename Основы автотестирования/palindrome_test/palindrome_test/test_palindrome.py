from palindrome import palindrome


# Check a palindrome string is a palindrome (positive)
def test_is_palindrome():
    # expect that method return True
    assert palindrome("abc.cba")


def test_is_not_palindrome():
    assert not palindrome("asdfg")
