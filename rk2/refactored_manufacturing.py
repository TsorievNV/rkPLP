"""
Рефакторированный код для рубежного контроля
Содержит классы и сервисы для работы с производителями и деталями
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
from collections import defaultdict

@dataclass
class Manufacturer:
    """Класс для представления производителя"""
    manufacturer_id: int
    manufacturer_name: str

@dataclass
class Detail:
    """Класс для представления детали"""
    detail_id: int
    detail_name: str
    price: float
    manufacturer_id: int

@dataclass
class ManufacturerDetail:
    """Класс для связи производителя и детали"""
    manufacturer_id: int
    detail_id: int


class ManufacturingService:
    """Сервис для работы с данными о производителях и деталях"""

    def __init__(self, manufacturers: List[Manufacturer],
                 details: List[Detail],
                 manufacturer_details: List[ManufacturerDetail]):
        self.manufacturers = manufacturers
        self.details = details
        self.manufacturer_details = manufacturer_details

    def get_manufacturers_dict(self) -> Dict[int, Manufacturer]:
        """Создает словарь производителей по ID"""
        return {m.manufacturer_id: m for m in self.manufacturers}

    def get_details_dict(self) -> Dict[int, Detail]:
        """Создает словарь деталей по ID"""
        return {d.detail_id: d for d in self.details}

    def get_manufacturer_to_details(self) -> Dict[int, List[int]]:
        """Создает словарь соответствия производителя и его деталей"""
        manufacturer_to_details = defaultdict(list)
        for md in self.manufacturer_details:
            manufacturer_to_details[md.manufacturer_id].append(md.detail_id)
        return manufacturer_to_details

    def get_details_by_manufacturer(self) -> List[Tuple[str, str, float]]:
        """Запрос 1: Получить детали с их производителями"""
        manufacturer_dict = self.get_manufacturers_dict()
        result = []

        for detail in sorted(self.details, key=lambda x: (x.manufacturer_id, x.detail_id)):
            manufacturer = manufacturer_dict.get(detail.manufacturer_id)
            if manufacturer:
                result.append((
                    manufacturer.manufacturer_name,
                    detail.detail_name,
                    detail.price
                ))
        return result

    def get_total_price_by_manufacturer(self) -> List[Tuple[str, float]]:
        """Запрос 2: Получить суммарную стоимость деталей по производителям"""
        price_totals = defaultdict(float)

        for detail in self.details:
            price_totals[detail.manufacturer_id] += detail.price

        manufacturer_dict = self.get_manufacturers_dict()
        result = []

        for manufacturer in self.manufacturers:
            total_price = price_totals.get(manufacturer.manufacturer_id, 0.0)
            result.append((manufacturer.manufacturer_name, total_price))

        # Сортировка по убыванию суммарной стоимости
        return sorted(result, key=lambda x: x[1], reverse=True)

    def get_department_manufacturers_with_details(self) -> Dict[str, List[Tuple[str, float]]]:
        """Запрос 3: Получить производителей с 'отдел' в названии и их детали"""
        manufacturer_dict = self.get_manufacturers_dict()
        detail_dict = self.get_details_dict()
        manufacturer_to_details = self.get_manufacturer_to_details()

        result = {}

        for manufacturer in self.manufacturers:
            if "отдел" in manufacturer.manufacturer_name.lower():
                detail_ids = manufacturer_to_details.get(manufacturer.manufacturer_id, [])
                details_list = []

                for detail_id in detail_ids:
                    if detail_id in detail_dict:
                        detail = detail_dict[detail_id]
                        details_list.append((detail.detail_name, detail.price))

                result[manufacturer.manufacturer_name] = details_list

        return result


# Данные для работы
def get_sample_data() -> Tuple[List[Manufacturer], List[Detail], List[ManufacturerDetail]]:
    """Возвращает тестовые данные"""
    manufacturers = [
        Manufacturer(1, "Основной производственный отдел"),
        Manufacturer(2, "Отдел металлообработки"),
        Manufacturer(3, "Электротехнический отдел"),
        Manufacturer(4, "Производитель электронных компонентов"),
        Manufacturer(5, "Отдел крепежных изделий")
    ]

    details = [
        Detail(1, "Болт М8", 15.50, 2),
        Detail(2, "Гайка М8", 8.30, 2),
        Detail(3, "Шайба 8мм", 5.20, 2),
        Detail(4, "Микроконтроллер ATmega328", 250.00, 4),
        Detail(5, "Резистор 100 Ом", 2.50, 4),
        Detail(6, "Конденсатор 10мкФ", 3.80, 4),
        Detail(7, "Винт саморез", 12.00, 5),
        Detail(8, "Дюбель пластиковый", 7.50, 5),
        Detail(9, "Подшипник 6000", 45.00, 1),
        Detail(10, "Шестерня модуль 1", 120.00, 1)
    ]

    manufacturer_details = [
        ManufacturerDetail(1, 9), ManufacturerDetail(1, 10),
        ManufacturerDetail(2, 1), ManufacturerDetail(2, 2), ManufacturerDetail(2, 3),
        ManufacturerDetail(3, 5), ManufacturerDetail(3, 6),
        ManufacturerDetail(4, 4), ManufacturerDetail(4, 5), ManufacturerDetail(4, 6),
        ManufacturerDetail(5, 7), ManufacturerDetail(5, 8)
    ]

    return manufacturers, details, manufacturer_details


# Старые функции для обратной совместимости
def task1_functional():
    """Запрос 1 в функциональном стиле"""
    manufacturers, details, manufacturer_details = get_sample_data()
    service = ManufacturingService(manufacturers, details, manufacturer_details)
    result = service.get_details_by_manufacturer()

    print("=== ЗАПРОС 1 (функциональный): Детали и производители ===")
    for manufacturer_name, detail_name, price in result:
        print(f"Производитель: {manufacturer_name} -> "
              f"Деталь: {detail_name}, Цена: {price} руб.")
    print()

def task2_functional():
    """Запрос 2 в функциональном стиле"""
    manufacturers, details, manufacturer_details = get_sample_data()
    service = ManufacturingService(manufacturers, details, manufacturer_details)
    result = service.get_total_price_by_manufacturer()

    print("=== ЗАПРОС 2 (функциональный): Суммарная стоимость ===")
    for manufacturer_name, total_price in result:
        print(f"Производитель: {manufacturer_name}, Суммарная стоимость: {total_price:.2f} руб.")
    print()

def task3_functional():
    """Запрос 3 в функциональном стиле"""
    manufacturers, details, manufacturer_details = get_sample_data()
    service = ManufacturingService(manufacturers, details, manufacturer_details)
    result = service.get_department_manufacturers_with_details()

    print("=== ЗАПРОС 3 (функциональный): Производители с 'отдел' в названии ===")
    for manufacturer_name, details_list in result.items():
        print(f"\nПроизводитель: {manufacturer_name}")
        if details_list:
            for detail_name, price in details_list:
                print(f"  - Деталь: {detail_name}, Цена: {price} руб.")
        else:
            print("  - Нет деталей")
    print()


if __name__ == "__main__":
    print("ФУНКЦИОНАЛЬНАЯ РЕАЛИЗАЦИЯ:")
    print("=" * 50)
    task1_functional()
    task2_functional()
    task3_functional()
