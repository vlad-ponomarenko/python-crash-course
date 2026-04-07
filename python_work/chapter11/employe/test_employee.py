import pytest
from employee import Employee


@pytest.fixture
def get_employee():
    e_1 = Employee("Alex", "Arkhipov", 5000)
    return e_1


def test_give_default_raise(get_employee):

    get_employee.give_raise()
    assert get_employee.annual_salary == 10000


def test_give_custom_raise(get_employee):
    get_employee.give_raise(20000)
    assert get_employee.annual_salary == 25000
