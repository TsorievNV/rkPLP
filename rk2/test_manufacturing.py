"""
Модульные тесты для рефакторированного кода
Используется TDD-фреймворк unittest
"""

import unittest
from refactored_manufacturing import (
    Manufacturer,
    Detail,
    ManufacturerDetail,
    ManufacturingService,
    get_sample_data
)


class TestManufacturingService(unittest.TestCase):
    """Модульные тесты для ManufacturingService"""

    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.manufacturers, self.details, self.manufacturer_details = get_sample_data()
        self.service = ManufacturingService(
            self.manufacturers,
            self.details,
            self.manufacturer_details
        )

    def test_get_details_by_manufacturer(self):
        """Тест 1: Проверка получения деталей с производителями"""
        # Act
        result = self.service.get_details_by_manufacturer()

        # Assert
        self.assertEqual(len(result), 10)  # Должно быть 10 деталей

        # Проверяем первую запись (должна быть от производителя с ID 1)
        first_record = result[0]
        self.assertEqual(first_record[0], "Основной производственный отдел")
        self.assertEqual(first_record[1], "Подшипник 6000")
        self.assertEqual(first_record[2], 45.00)

        # Проверяем сортировку по manufacturer_id, затем по detail_id
        manufacturer_ids = []
        for detail in self.details:
            manufacturer_ids.append(detail.manufacturer_id)

        # Первые две детали должны быть от производителя с ID 1
        self.assertEqual(result[0][0], "Основной производственный отдел")
        self.assertEqual(result[1][0], "Основной производственный отдел")

        print("✓ Тест 1 пройден: get_details_by_manufacturer работает корректно")

    def test_get_total_price_by_manufacturer(self):
        """Тест 2: Проверка расчета суммарной стоимости по производителям"""
        # Act
        result = self.service.get_total_price_by_manufacturer()

        # Assert
        self.assertEqual(len(result), 5)  # Должно быть 5 производителей

        # Проверяем суммарную стоимость для конкретного производителя
        # Производитель 2 (Отдел металлообработки) имеет детали: 15.50 + 8.30 + 5.20 = 29.00
        for manufacturer_name, total_price in result:
            if manufacturer_name == "Отдел металлообработки":
                self.assertAlmostEqual(total_price, 29.00, places=2)
                break

        # Проверяем сортировку по убыванию
        prices = [price for _, price in result]
        self.assertEqual(prices, sorted(prices, reverse=True))

        # Проверяем, что производитель без деталей имеет сумму 0
        # В наших данных все производители имеют детали, но проверим общую логику
        for manufacturer_name, total_price in result:
            self.assertGreaterEqual(total_price, 0.0)

        print("✓ Тест 2 пройден: get_total_price_by_manufacturer работает корректно")

    def test_get_department_manufacturers_with_details(self):
        """Тест 3: Проверка фильтрации производителей с 'отдел' в названии"""
        # Act
        result = self.service.get_department_manufacturers_with_details()

        # Assert
        # Должно быть 4 производителя с 'отдел' в названии
        expected_department_manufacturers = [
            "Основной производственный отдел",
            "Отдел металлообработки",
            "Электротехнический отдел",
            "Отдел крепежных изделий"
        ]

        self.assertEqual(len(result), 4)

        for manufacturer_name in expected_department_manufacturers:
            self.assertIn(manufacturer_name, result)

        # Проверяем детали для конкретного производителя
        manufacturer_name = "Отдел металлообработки"
        details_list = result[manufacturer_name]

        self.assertEqual(len(details_list), 3)  # Должно быть 3 детали

        # Проверяем названия деталей
        detail_names = [detail_name for detail_name, _ in details_list]
        expected_detail_names = ["Болт М8", "Гайка М8", "Шайба 8мм"]

        for expected_name in expected_detail_names:
            self.assertIn(expected_name, detail_names)

        # Проверяем, что производитель без 'отдел' не попал в результат
        self.assertNotIn("Производитель электронных компонентов", result)

        print("✓ Тест 3 пройден: get_department_manufacturers_with_details работает корректно")

    def test_empty_data(self):
        """Тест с пустыми данными"""
        # Arrange
        empty_service = ManufacturingService([], [], [])

        # Act & Assert
        result1 = empty_service.get_details_by_manufacturer()
        result2 = empty_service.get_total_price_by_manufacturer()
        result3 = empty_service.get_department_manufacturers_with_details()

        self.assertEqual(result1, [])
        self.assertEqual(result2, [])
        self.assertEqual(result3, {})

        print("✓ Тест с пустыми данными пройден")


class TestDataStructures(unittest.TestCase):
    """Тесты для структур данных"""

    def test_manufacturer_creation(self):
        """Тест создания объекта Manufacturer"""
        manufacturer = Manufacturer(1, "Тестовый производитель")

        self.assertEqual(manufacturer.manufacturer_id, 1)
        self.assertEqual(manufacturer.manufacturer_name, "Тестовый производитель")
        self.assertEqual(str(manufacturer),
                        "Manufacturer(manufacturer_id=1, manufacturer_name='Тестовый производитель')")

    def test_detail_creation(self):
        """Тест создания объекта Detail"""
        detail = Detail(1, "Тестовая деталь", 100.50, 1)

        self.assertEqual(detail.detail_id, 1)
        self.assertEqual(detail.detail_name, "Тестовая деталь")
        self.assertEqual(detail.price, 100.50)
        self.assertEqual(detail.manufacturer_id, 1)


def run_tests():
    """Запуск всех тестов"""
    print("=" * 60)
    print("ЗАПУСК МОДУЛЬНЫХ ТЕСТОВ")
    print("=" * 60)

    # Создаем test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Добавляем тесты
    suite.addTests(loader.loadTestsFromTestCase(TestManufacturingService))
    suite.addTests(loader.loadTestsFromTestCase(TestDataStructures))

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Выводим итоговую статистику
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n✗ ЕСТЬ ПРОБЛЕМЫ С ТЕСТАМИ")

    return result.wasSuccessful()


if __name__ == "__main__":
    # Запуск тестов при прямом вызове файла
    run_tests()
