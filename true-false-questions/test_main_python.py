import pytest
from main_python import random_question, user_input


def test_random_question():
    assert random_question(
        "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/python-car-test-data/true-false-questions/output/output3_all_pages.csv",
    ) == {
        "Number": "641",
        "Answer": "O",
        "Question": "When a driver causes no injury or death in an accident but does not act according\nto the regulations, the driver will be fined between NT$1,000 and NT$3,000; if\nthe driver escapes from the scene, the driver's license will be suspended for 1 to\n3 month(s).",
    }


def test_user_input():
    assert user_input("X") == "X"


pytest.main(["-v", "--tb=line", "-rN", __file__])
