class SubnetRange:
    """Клас для роботи з діапазонами IP-підмереж."""
    def __init__(self, start_ip: int, end_ip: int):
        if start_ip > end_ip:
            raise ValueError("Початкова IP-адреса не може перевищувати кінцеву.")
        self.start_ip = start_ip
        self.end_ip = end_ip

    def __str__(self) -> str:
        return f"Діапазон мережі [IP ID від {self.start_ip} до {self.end_ip}]"

    def __repr__(self) -> str:
        return f"SubnetRange(start_ip={self.start_ip}, end_ip={self.end_ip})"

    def __len__(self) -> int:
        return (self.end_ip - self.start_ip) + 1

    def __add__(self, other: 'SubnetRange') -> 'SubnetRange':
        if not isinstance(other, SubnetRange):
            return NotImplemented
        new_start = min(self.start_ip, other.start_ip)
        new_end = max(self.end_ip, other.end_ip)
        return SubnetRange(new_start, new_end)

    def __sub__(self, other: int) -> 'SubnetRange':
        if not isinstance(other, int):
            return NotImplemented
        new_end = max(self.start_ip, self.end_ip - other)
        return SubnetRange(self.start_ip, new_end)

    def __eq__(self, other: 'SubnetRange') -> bool:
        if not isinstance(other, SubnetRange):
            return False
        return self.start_ip == other.start_ip and self.end_ip == other.end_ip

    def __getitem__(self, index: int) -> int:
        length = len(self)
        if index < 0:
            index += length
        if not (0 <= index < length):
            raise IndexError("Індекс за межами діапазону підмережі.")
        return self.start_ip + index


if __name__ == "__main__":
    sub1 = SubnetRange(100, 110)
    sub2 = SubnetRange(105, 120)

    print(f"str(sub1): {sub1}")
    print(f"repr(sub1): {sub1!r}")
    print(f"len(sub1): {len(sub1)}")

    combined = sub1 + sub2
    print(f"sub1 + sub2: {combined}")

    reduced = sub2 - 5
    print(f"sub2 - 5: {reduced}")

    sub_copy = SubnetRange(100, 110)
    print(f"sub1 == sub_copy: {sub1 == sub_copy}")
    print(f"sub1 == sub2: {sub1 == sub2}")

    print(f"sub1[2]: {sub1[2]}")
    print(f"sub1[-1]: {sub1[-1]}")
