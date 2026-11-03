# Task 2.1: No error occurred because Notifier was concrete and implemented a dummy send() with pass, so the typo inherited the parent's do-nothing method.
# Task 2.3: send() is abstract, while notify() is concrete.

from abc import ABC, abstractmethod
import pytest


class Notifier(ABC):
  max_length = 1000

  @abstractmethod
  def send(self, recipient, text):
    pass

  def notify(self, recipient, text):
    self.send(recipient, text[: self.max_length])


class TelegramNotifier(Notifier):
  max_length = 4096

  def send(self, recipient, text):
    print(f"telegram -> {recipient}: {text}")


class SmsNotifier(Notifier):
  max_length = 160

  def send(self, recipient, text):
    print(f"sms -> {recipient}: {text}")


# Tests
def test_abstract_enforcement():
  class BrokenNotifier(Notifier):
    def sned(self, recipient, text):
      pass

  with pytest.raises(TypeError):
    BrokenNotifier()


def test_sms_length_limit(capsys):
  sms = SmsNotifier()
  long_text = "A" * 200
  sms.notify("+998901234567", long_text)
  captured = capsys.readouterr()
  # Ensures text passed to send is sliced to max_length (160)
  assert "A" * 160 in captured.out