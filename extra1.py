from collections import UserDict

class Headers(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __init__(self, initialdata=None, **kwargs):
        super().__init__()
        if initialdata is not None:
            self.update(initialdata)
        if kwargs:
            self.update(kwargs)

# Testing the fix:
h = Headers({"Accept": "application/json"})
h["Content-Type"] = "text/plain"
h.update({"Content-Type": "application/json"})
h.setdefault("X-Request-Id", "42")
print(h)
# Output: {'accept': 'application/json', 'content-type': 'application/json', 'x-request-id': '42'}
class Headers(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __delitem__(self, key):
        super().__delitem__(key.lower())

    def __contains__(self, key):
        return super().__contains__(key.lower())

    def get(self, key, default=None):
        return super().get(key.lower(), default)

    def pop(self, key, *args):
        return super().pop(key.lower(), *args)