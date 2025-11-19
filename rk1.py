from dataclasses import dataclass
from typing import List
from collections import defaultdict

@dataclass
class Manufacturer:
    manufacturer_id: int
    manufacturer_name: str

@dataclass
class Detail:
    detail_id: int
    detail_name: str
    price: float
    manufacturer_id: int

@dataclass
class ManufacturerDetail:
    manufacturer_id: int
    detail_id: int

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

def task1_functional():
    """Запрос 1 в функциональном стиле"""
    manufacturer_dict = {m.manufacturer_id: m for m in manufacturers}

    print("=== ЗАПРОС 1 (функциональный): Детали и производители ===")
    [print(f"Производитель: {manufacturer_dict[d.manufacturer_id].manufacturer_name} -> "
           f"Деталь: {d.detail_name}, Цена: {d.price} руб.")
     for d in sorted(details, key=lambda x: (x.manufacturer_id, x.detail_id))]
    print()

def task2_functional():
    """Запрос 2 в функциональном стиле"""
    price_totals = defaultdict(float)
    for detail in details:
        price_totals[detail.manufacturer_id] += detail.price

    print("=== ЗАПРОС 2 (функциональный): Суммарная стоимость ===")
    [print(f"Производитель: {m.manufacturer_name}, Суммарная стоимость: {price_totals[m.manufacturer_id]:.2f} руб.")
     for m in sorted(manufacturers, key=lambda x: price_totals[x.manufacturer_id], reverse=True)]
    print()

def task3_functional():
    """Запрос 3 в функциональном стиле"""

    manufacturer_to_details = defaultdict(list)
    for md in manufacturer_details:
        manufacturer_to_details[md.manufacturer_id].append(md.detail_id)

    detail_dict = {d.detail_id: d for d in details}

    print("=== ЗАПРОС 3 (функциональный): Производители с 'отдел' в названии ===")
    department_manufacturers = filter(lambda m: "отдел" in m.manufacturer_name.lower(), manufacturers)

    for manufacturer in department_manufacturers:
        print(f"\nПроизводитель: {manufacturer.manufacturer_name}")
        detail_ids = manufacturer_to_details.get(manufacturer.manufacturer_id, [])
        manufacturer_details_list = [detail_dict[did] for did in detail_ids if did in detail_dict]

        if manufacturer_details_list:
            [print(f"  - Деталь: {d.detail_name}, Цена: {d.price} руб.") for d in manufacturer_details_list]
        else:
            print("  - Нет деталей")
    print()

if __name__ == "__main__":
    print("ФУНКЦИОНАЛЬНАЯ РЕАЛИЗАЦИЯ:")
    print("=" * 50)
    task1_functional()
    task2_functional()
    task3_functional()
