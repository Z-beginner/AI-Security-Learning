import pytest

from Q11_3 import Employee

def test_give_default_raise():
    employee = Employee("John", "Doe", 11111)
    employee.give_raise()
    assert employee.annual_salary == 16111
def test_give_custom_raise():
    employee = Employee("John", "Doe", 22222)
    employee.give_raise(3000)
    assert employee.annual_salary == 25222

@pytest.fixture
def employee():
    return Employee("John", "Doe", 11111)
def test_give_default_raise1(employee):
    employee.give_raise()
    assert employee.annual_salary == 16111
def test_give_custom_raise2(employee):
    employee.give_raise(3000)
    assert employee.annual_salary == 14111