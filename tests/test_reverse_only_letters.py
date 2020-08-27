import pytest
from puzzles.reverse_only_letters import reverse_only_letters


def test_reverse_only_letters():
    assert reverse_only_letters("ab-cd") == "dc-ba"
    assert reverse_only_letters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert reverse_only_letters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
