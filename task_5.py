from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    """Абстрактний інтерфейс стратегії."""
    @abstractmethod
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        pass


class CourierShipping(ShippingStrategy):
    """Доставка кур'єром."""
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        return 100.0 + (weight_kg * 15.0) + (distance_km * 5.0)


class PostMachineShipping(ShippingStrategy):
    """Доставка у поштомат."""
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        if weight_kg > 20.0:
            raise ValueError("Вантаж понад 20 кг не приймається.")
        return 60.0 + (distance_km * 2.0)


class PickupShipping(ShippingStrategy):
    """Самовивіз."""
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        return 0.0


class DroneExpressShipping(ShippingStrategy):
    """Доставка дроном."""
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        if weight_kg > 5.0:
            raise ValueError("Вантаж понад 5 кг не приймається.")
        return 250.0 + (distance_km * 25.0)


class OrderDeliveryContext:
    """Контекст замовлення."""
    def __init__(self, order_id: str, weight_kg: float, distance_km: float, strategy: ShippingStrategy):
        self.order_id = order_id
        self.weight_kg = weight_kg
        self.distance_km = distance_km
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def compute_total_shipping(self) -> float:
        return self._strategy.calculate_cost(self.weight_kg, self.distance_km)


if __name__ == "__main__":
    order = OrderDeliveryContext("ORD-9881", weight_kg=4.5, distance_km=30.0, strategy=CourierShipping())
    print(f"Доставка кур'єром: {order.compute_total_shipping():.2f} грн")

    order.set_strategy(PostMachineShipping())
    print(f"Поштомат: {order.compute_total_shipping():.2f} грн")

    order.set_strategy(PickupShipping())
    print(f"Самовивіз: {order.compute_total_shipping():.2f} грн")

    order.set_strategy(DroneExpressShipping())
    print(f"Доставка дроном: {order.compute_total_shipping():.2f} грн")
