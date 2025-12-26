"""
Демонстрация работы рефакторинга и тестов
"""

from refactored_manufacturing import (
    get_sample_data,
    ManufacturingService,
    task1_functional,
    task2_functional,
    task3_functional
)


def demonstrate_refactored_code():
    """Демонстрация работы рефакторированного кода"""
    print("ДЕМОНСТРАЦИЯ РЕФАКТОРИНГА")
    print("=" * 60)

    # Получаем данные
    manufacturers, details, manufacturer_details = get_sample_data()

    # Создаем сервис
    service = ManufacturingService(manufacturers, details, manufacturer_details)

    # Демонстрируем каждый метод
    print("\n1. Детали с производителями:")
    print("-" * 40)
    details_by_manufacturer = service.get_details_by_manufacturer()
    for i, (manufacturer, detail, price) in enumerate(details_by_manufacturer[:3], 1):
        print(f"{i}. {manufacturer} -> {detail} ({price} руб.)")
    print(f"... и еще {len(details_by_manufacturer) - 3} записей")

    print("\n2. Суммарная стоимость по производителям:")
    print("-" * 40)
    total_prices = service.get_total_price_by_manufacturer()
    for manufacturer, total in total_prices:
        print(f"{manufacturer}: {total:.2f} руб.")

    print("\n3. Производители с 'отдел' в названии:")
    print("-" * 40)
    department_manufacturers = service.get_department_manufacturers_with_details()
    for manufacturer, details_list in department_manufacturers.items():
        print(f"\n{manufacturer}:")
        for detail, price in details_list[:2]:  # Показываем первые 2 детали
            print(f"  - {detail} ({price} руб.)")
        if len(details_list) > 2:
            print(f"  ... и еще {len(details_list) - 2} деталей")


def demonstrate_original_functionality():
    """Демонстрация исходной функциональности"""
    print("\n\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ИСХОДНОЙ ФУНКЦИОНАЛЬНОСТИ")
    print("=" * 60)

    task1_functional()
    task2_functional()
    task3_functional()


if __name__ == "__main__":
    # Демонстрируем рефакторинг
    demonstrate_refactored_code()

    # Демонстрируем исходную функциональность
    demonstrate_original_functionality()
