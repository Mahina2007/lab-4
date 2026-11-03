# Task 6.1: export_report actually needs behavior (the presence of a write(data: bytes) method) rather than a specific class type.
# Task 6.4: Static type checkers like mypy catch protocol mismatches before runtime by checking if targets implement required methods.

import io
from typing import Iterable, Protocol


class Writable(Protocol):

  def write(self, data: bytes) -> int:
    ...


def export_report(rows: Iterable[Iterable], target: Writable):
  for r in rows:
    target.write((",".join(map(str, r)) + "\n").encode())


class S3Upload:

  def __init__(self, bucket: str, key: str):
    self.bucket, self.key = bucket, key
    self.parts = []

  def write(self, data: bytes) -> int:
    self.parts.append(data)
    return len(data)


# Tests
def test_export_to_bytes_io():
  buf = io.BytesIO()
  export_report([[1, 2], [3, 4]], buf)
  assert buf.getvalue() == b"1,2\n3,4\n"


def test_export_to_s3():
  s3 = S3Upload("my-bucket", "report.csv")
  export_report([["a", "b"], ["c", "d"]], s3)
  assert s3.parts == [b"a,b\n", b"c,d\n"]