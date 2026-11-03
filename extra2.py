import inspect


class PaymentMethod:
    REGISTRY = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)

        # Abstract middle classes may skip the name
        if inspect.isabstract(cls):
            return

        if not name:
            raise TypeError(f"Concrete payment class {cls.__name__} must define a 'name' parameter in its header.")

        if name in cls.REGISTRY:
            raise ValueError(
                f"Duplicate payment method name '{name}' found in {cls.__name__} (already registered by {cls.REGISTRY[name].__name__}).")

        cls.REGISTRY[name] = cls


# Example Concrete Subclass:
class Click(PaymentMethod, name="click"):
    pass