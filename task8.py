# Task 8.1: In Python, function definitions overwrite each other; the class retains only the last defined version under the name search.
# Task 8.2: Mutable default arguments (like filters={}) must not be used because the dictionary object would be shared across all function calls.


class ProductSearch:

  def __init__(self, products):
    self.products = products

  def search(self, query: str, filters: dict = None):
    q = query.lower()
    result = [p for p in self.products if q in p["title"].lower()]
    if filters:
      for key, value in filters.items():
        result = [p for p in result if p.get(key) == value]
    return result


# Tests
def test_product_search():
  ps = ProductSearch([
      {"title": "iPhone 15", "brand": "Apple"},
      {"title": "Galaxy S24", "brand": "Samsung"},
  ])

  res1 = ps.search("iphone")
  assert len(res1) == 1

  res2 = ps.search("iphone", {"brand": "Apple"})
  assert len(res2) == 1

  res3 = ps.search("iphone", {"brand": "Samsung"})
  assert len(res3) == 0