def is_palindrome_v1(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1("noon")
    True
    >>> is_palindrome_v1("racrcar")
    True
    >>> is_palindrome_v1("dented")
    False
    """
    return reverse(s) == s

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse("a")
    a
    >>> reverse("apple")
    elppa
    """
    rev = ""
    # For each character in s, add that character to the beginning of rev.
    for ch in s:
        rev = ch + rev
    return rev

def is_palindrome_v2(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2("noon")
    True
    >>> is_palindrome_v2("racrcar")
    True
    >>> is_palindrome_v2("dented")
    False
    """
     # The number of chars in s.
    n = len(s)
    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n//2] == reverse(s[n-n//2:])

def is_palindrome_v3(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3("noon")
    True
    >>> is_palindrome_v3("racrcar")
    True
    >>> is_palindrome_v3("dented")
    False
    """
    # s[i] and s[j] are the next pair of characters to compare.
    i = 0
    j = len(s) -1

    # The characters in s[:i] have been successfully compared to those in s[j:].
    while i <  j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return i >= j

def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """
    count = 0

    for item in L:
        if item.startswith(ch):
<<<<<<< HEAD
            count = count + 1

=======
>>>>>>> 8fcd2b1b35f96ecc26ddda6bf0b32eba382c203f
    return count
print(count_startswith(['rumba', 'salsa', 'samba'], 's'))

def calvins_function():
    print("Calvin was here!!")
