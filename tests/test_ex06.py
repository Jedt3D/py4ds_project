from src.ex06 import *

"""
The ordinal suffix depends on the last two digits in the number:
    * If the last two digits end with 11, 12, or 13 then the suffix is ―th.
    * If the number ends with 1, the suffix is ―st.
    * If the number ends with 2, the suffix is ―nd.
    * If the number ends with 3, the suffix is ―rd.
    * Every other number has a suffix of ―th.
"""


def test_ordinal_suffix():
    assert ordinal_suffix(0) == '0th'
    assert ordinal_suffix(1) == '1st'
    assert ordinal_suffix(2) == '2nd'
    assert ordinal_suffix(3) == '3rd'
    assert ordinal_suffix(4) == '4th'
    assert ordinal_suffix(10) == '10th'
    assert ordinal_suffix(11) == '11th'
    assert ordinal_suffix(12) == '12th'
    assert ordinal_suffix(13) == '13th'
    assert ordinal_suffix(14) == '14th'
    assert ordinal_suffix(101) == '101st'
