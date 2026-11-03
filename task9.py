# Task 9.1: Method Resolution Order (MRO) governs super() chains. If a mixin omits super().save(), the chain breaks and base persistence is skipped.
# Task 9.3: Validation must raise an exception rather than silently returning false, otherwise subsequent code executes with invalid state.


class Model:

  def save(self):
    print("Model.save: INSERT/UPDATE")


class TimestampMixin:

  def save(self):
    print("TimestampMixin: set updated_at")
    super().save()


class ValidateMixin:

  def save(self):
    print("ValidateMixin: validate fields")
    super().save()


class AuditMixin:

  def save(self):
    super().save()
    print("AuditMixin: write audit entry")


class Invoice(TimestampMixin, ValidateMixin, AuditMixin, Model):
  pass


# Tests
def test_invoice_save_mro(capsys):
  inv = Invoice()
  inv.save()
  captured = capsys.readouterr().out

  lines = captured.strip().split("\n")
  assert "TimestampMixin" in lines[0]
  assert "ValidateMixin" in lines[1]