# Task 4.1: AuditLog is not a list because inheriting from list breaks LSP and exposes dangerous mutation methods like clear(), pop(), and sort().
# Task 4.4: Overriding clear() or pop() is worse because list has too many public mutation methods that remain exposed and vulnerable.

import pytest


class AuditLog:

  def __init__(self):
    self._entries = []

  def record(self, user: str, action: str):
    self._entries.append((user, action))

  def __len__(self):
    return len(self._entries)

  def __iter__(self):
    return iter(self._entries)

  def last(self, n: int):
    return self._entries[-n:]


# Tests
def test_audit_log_protection():
  log = AuditLog()
  log.record("admin", "approve_loan#77")

  assert len(log) == 1
  for entry in log:
    assert entry == ("admin", "approve_loan#77")

  with pytest.raises(AttributeError):
    log.clear()

  with pytest.raises(AttributeError):
    log.pop()