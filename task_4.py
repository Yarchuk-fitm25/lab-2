from abc import ABC, abstractmethod
import datetime

class SecurityEventLogger:
    """Компонент логування подій безпеки."""
    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[SECURITY LOG {timestamp}]: {message}")


class BaseSensor(ABC):
    """Абстрактний базовий клас для всіх датчиків."""
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id

    @property
    @abstractmethod
    def sensor_type(self) -> str:
        pass

    @abstractmethod
    def scan_environment(self) -> bool:
        pass

    def get_info(self) -> str:
        return f"Датчик ID: {self.sensor_id} [Тип: {self.sensor_type}]"


class MotionSensor(BaseSensor):
    """Датчик руху."""
    @property
    def sensor_type(self) -> str:
        return "Інфрачервоний датчик руху"

    def scan_environment(self) -> bool:
        return False


class BiometricAccessScanner(BaseSensor, ABC):
    """Проміжний абстрактний клас."""
    pass


class FingerprintScanner(BiometricAccessScanner):
    """Сканер відбитків пальців."""
    @property
    def sensor_type(self) -> str:
        return "Біометричний сканер відбитків"

    def scan_environment(self) -> bool:
        return True


class SecurityControlPanel:
    """Панель керування безпекою (композиція)."""
    def __init__(self, location: str):
        self.location = location
        self._logger = SecurityEventLogger()
        self._sensors: list[BaseSensor] = []

    def add_sensor(self, sensor: BaseSensor):
        self._sensors.append(sensor)
        self._logger.log(f"Додано новий датчик {sensor.sensor_id} до секції '{self.location}'.")

    def run_system_check(self):
        self._logger.log(f"Запуск перевірки для секції '{self.location}'...")
        for sensor in self._sensors:
            print(f" -> {sensor.get_info()}")
            alert = sensor.scan_environment()
            if alert:
                self._logger.log(f"УВАГА! Тривога на датчику {sensor.sensor_id}!")
            else:
                self._logger.log(f"Стан датчика {sensor.sensor_id} у нормі.")


if __name__ == "__main__":
    try:
        invalid_sensor = BaseSensor("TEST-00")
    except TypeError as e:
        print(f"Помилка інстанціювання ABC: {e}")

    panel = SecurityControlPanel("Зона-Б (Серверна №2)")
    motion = MotionSensor("MS-801")
    fp_scanner = FingerprintScanner("FP-102")

    panel.add_sensor(motion)
    panel.add_sensor(fp_scanner)
    panel.run_system_check()
