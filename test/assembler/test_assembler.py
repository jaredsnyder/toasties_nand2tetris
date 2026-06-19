import pytest
from assembler import assemble

def test_assemble():
    lines = ["..."]
    out = assemble(lines)
    assert out is not None


def test_assembler_add():
    input_lines = [
        "@2\n",
        "D=A\n",
    ]
    expected = (
        "0000000000000010\n"
        "1110110000010000\n"
    )
    assert assemble(input_lines) == expected