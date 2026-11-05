class LibraryItem:
    """Базовий клас для елементів бібліотечного фонду."""
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    def get_checkout_period(self) -> int:
        return 14

    def __str__(self) -> str:
        return f"«{self.title}» ({self.year})"


class Book(LibraryItem):
    """Клас друкованої книги."""
    def __init__(self, title: str, year: int, author: str, pages: int):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def get_checkout_period(self) -> int:
        return 30

    def __str__(self) -> str:
        return f"Книга: {super().__str__()}, автор: {self.author}, сторінок: {self.pages}"


class Magazine(LibraryItem):
    """Клас періодичного журналу."""
    def __init__(self, title: str, year: int, issue_number: int):
        super().__init__(title, year)
        self.issue_number = issue_number

    def get_checkout_period(self) -> int:
        return 7

    def __str__(self) -> str:
        return f"Журнал: {super().__str__()}, випуск №{self.issue_number}"


class DigitalThesis(LibraryItem):
    """Клас цифрової студентської дисертації."""
    def __init__(self, title: str, year: int, student_name: str, file_size_mb: float):
        super().__init__(title, year)
        self.student_name = student_name
        self.file_size_mb = file_size_mb

    def get_checkout_period(self) -> int:
        return 365

    def __str__(self) -> str:
        return f"Дисертація: {super().__str__()}, автор(ка): {self.student_name}, файл: {self.file_size_mb}MB"


if __name__ == "__main__":
    catalog = [
        Book("Безпека веб-додатків", 2024, "О. В. Коваль", 320),
        Magazine("Хакер (Україна)", 2026, 4),
        DigitalThesis("Аналіз стійкості алгоритмів RSA", 2025, "Ярчук А.І.", 14.5)
    ]

    for item in catalog:
        print(item)
        print(f" -> Термін видачі/доступу: {item.get_checkout_period()} днів\n")

    b = catalog[0]
    print(f"isinstance(b, Book): {isinstance(b, Book)}")
    print(f"isinstance(b, LibraryItem): {isinstance(b, LibraryItem)}")
    print(f"issubclass(DigitalThesis, LibraryItem): {issubclass(DigitalThesis, LibraryItem)}")
    print(f"issubclass(Magazine, Book): {issubclass(Magazine, Book)}")
