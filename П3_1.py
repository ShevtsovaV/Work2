class CustomList:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер должен быть положительным целым числом.")
        self.size = size
        self.items = [None] * size
        self.write_access_count = 0
        self.read_access_count = 0

    def get_write_access_count(self):
        return self.write_access_count

    def get_read_access_count(self):
        return self.read_access_count

    def set_value(self, index, value):
        if not -100 <= value <= 100:
            raise ValueError(f"Значение {value} выходит за пределы. Оно должно быть от -100 до 100.")
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} выходит за пределы.")
        self.items[index] = value
        self.write_access_count += 1

    def get_value(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} выходит за пределы.")
        self.read_access_count += 1
        return self.items[index]

    def print_all(self):
        print(self.items)

    def append(self, value):
        if not -100 <= value <= 100:
            raise ValueError(f"Значение {value} выходит за пределы. Оно должно быть от -100 до 100.")
        if None in self.items:
            for i in range(self.size):
                if self.items[i] is None:
                    self.items[i] = value
                    self.write_access_count += 1
                    return
        else:
            self.size += 1
            self.items.append(value)
            self.write_access_count += 1

    def add(self, other):
        if not isinstance(other, CustomList):
            raise TypeError("Другой список должен быть экземпляром CustomList.")
        
        max_len = max(self.size, other.size)
        result = CustomList(max_len)
        
        for i in range(max_len):
            a_value = self.items[i] if i < self.size and self.items[i] is not None else 0
            b_value = other.items[i] if i < other.size and other.items[i] is not None else 0
            result.set_value(i, a_value + b_value)
        
        return result

    def subtract(self, other):
        if not isinstance(other, CustomList):
            raise TypeError("Другой список должен быть экземпляром CustomList.")

        max_len = max(self.size, other.size)
        result = CustomList(max_len)

        for i in range(max_len):
            a_value = self.items[i] if i < self.size and self.items[i] is not None else 0
            b_value = other.items[i] if i < other.size and other.items[i] is not None else 0
            result.set_value(i, a_value - b_value)

        return result

if __name__ == "__main__":
    list_a = CustomList(3)
    list_a.set_value(0, 10)
    list_a.set_value(1, 20)

    list_b = CustomList(2)
    list_b.set_value(0, 5)
    list_b.set_value(1, 15)

    print("Список А:")
    list_a.print_all()
    print("Список Б:")
    list_b.print_all()

    result_add = list_a.add(list_b)
    print("Сложение списков А и Б:")
    result_add.print_all()

    result_subtract = list_a.subtract(list_b)
    print("Вычитание списка Б из списка А:")
    result_subtract.print_all()

    print("Количество записей в списке А:", list_a.get_write_access_count())
    print("Количество чтений в списке А:", list_a.get_read_access_count())