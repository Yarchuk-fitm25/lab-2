import re

class UserProfile:
    """Клас профілю користувача з інкапсуляцією та валідацією."""
    def __init__(self, username: str, email: str, rating: float):
        self._username = username
        self.__email = ""
        self.email = email
        self.__rating = 0.0
        self.rating = rating

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Email повинен бути рядком.")
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, value):
            raise ValueError(f"Некоректний формат електронної пошти: '{value}'.")
        self.__email = value

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Рейтинг повинен бути числовим значенням.")
        if not (0.0 <= value <= 100.0):
            raise ValueError(f"Рейтинг має бути в межах від 0.0 до 100.0, передано: {value}.")
        self.__rating = float(value)

    @property
    def status(self) -> str:
        if self.__rating >= 85.0:
            return "Експерт"
        elif self.__rating >= 50.0:
            return "Активний користувач"
        else:
            return "Новачок"

    def __str__(self) -> str:
        return f"Користувач '{self._username}' [{self.email}], рейтинг: {self.rating} ({self.status})"


if __name__ == "__main__":
    user = UserProfile("anastasiia_y", "ailysenkofitm25@kubg.edu.ua", 92.5)
    print(user)

    print(f"Поточний статус: {user.status}")
    user.rating = 45.0
    print(f"Новий статус після зміни рейтингу: {user.status}")

    try:
        user.rating = 150.0
    except ValueError as e:
        print(f"Помилка рейтингу: {e}")

    try:
        user.email = "invalid-email"
    except ValueError as e:
        print(f"Помилка email: {e}")

    try:
        print(user.__email)
    except AttributeError as e:
        print(f"Спроба прямого доступу: {e}")

    print(f"Доступ через Name Mangling: {user._UserProfile__email}")
