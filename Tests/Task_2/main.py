import pytest
from decode import decode


@pytest.mark.parametrize(
    "s,exp",
    [
        ("STRING", "... - .-. .. -. --."),
        ("123", ".---- ..--- ...--"),
        (".... . .-.. .-.. ---", "HELLO"),
    ],
)
def test_decode(s, exp):
    assert s == decode(exp)
