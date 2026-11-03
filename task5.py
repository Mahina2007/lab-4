# Task 5.1: "A lecturer is an employee" is not true for the entire life of the object because promotions change an employee's role, not their core identity (emp_id).
# Task 5.4: An employee has a role history relationship (composition/aggregation of historical role records).

from datetime import date


class Role:

  def monthly_pay(self) -> int:
    raise NotImplementedError


class LecturerRole(Role):

  def __init__(self, hours: int):
    self.hours = hours

  def monthly_pay(self) -> int:
    return self.hours * 120_000


class HeadRole(Role):

  def __init__(self, salary: int):
    self.salary = salary

  def monthly_pay(self) -> int:
    return self.salary + 3_000_000


class Employee:

  def __init__(self, emp_id: int, name: str, initial_role: Role):
    self.emp_id = emp_id
    self.name = name
    self.role_history = [(initial_role, date.today())]

  def change_role(self, new_role: Role):
    self.role_history.append((new_role, date.today()))

  def monthly_pay(self, history_index: int = -1) -> int:
    role, _ = self.role_history[history_index]
    return role.monthly_pay()


# Tests
def test_employee_promotion():
  emp = Employee(1, "Aziz", LecturerRole(100))
  assert emp.monthly_pay() == 12_000_000

  emp.change_role(HeadRole(14_000_000))
  assert emp.monthly_pay() == 17_000_000
  assert emp.monthly_pay(0) == 12_000_000