import logging

class EventRegistry:
    REGISTRY = {}

    @classmethod
    def register(cls, type_name):
        def decorator(subclass):
            cls.REGISTRY[type_name] = subclass
            return subclass
        return decorator

@EventRegistry.register("order_placed")
class OrderPlaced:
    def __init__(self, order_id, total_tiyin, currency, promo_code=None, version=1):
        self.order_id = order_id
        self.total_tiyin = total_tiyin
        self.currency = currency
        self.promo_code = promo_code
        self.version = version

    def to_dict(self):
        return {
            "type": "order_placed",
            "version": self.version,
            "order_id": self.order_id,
            "total_tiyin": self.total_tiyn,
            "currency": self.currency,
            "promo_code": self.promo_code
        }

    @classmethod
    def from_dict(cls, data):
        # Ignore unknown keys (forward compatibility for newer fields)
        valid_keys = {"order_id", "total_tiyin", "currency", "promo_code", "version"}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)

@EventRegistry.register("order_cancelled")
class OrderCancelled:
    def __init__(self, order_id, reason, version=1):
        self.order_id = order_id
        self.reason = reason
        self.version = version

    def to_dict(self):
        return {"type": "order_cancelled", "version": self.version, "order_id": self.order_id, "reason": self.reason}

    @classmethod
    def from_dict(cls, data):
        return cls(order_id=data.get("order_id"), reason=data.get("reason"), version=data.get("version", 1))

def decode(payload):
    event_type = payload.get("type")
    event_cls = EventRegistry.REGISTRY.get(event_type)
    if not event_cls:
        logging.warning(f"Unknown event type received and skipped: {event_type}")
        return None
    return event_cls.from_dict(payload)