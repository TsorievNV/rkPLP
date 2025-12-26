"""
Запуск всех демонстраций и тестов
"""

if __name__ == "__main__":
    print("РУБЕЖНЫЙ КОНТРОЛЬ: РЕФАКТОРИНГ И ТЕСТИРОВАНИЕ")
    print("=" * 60)

    # Демонстрация рефакторинга
    from main_demo import (
        demonstrate_refactored_code,
        demonstrate_original_functionality
    )

    demonstrate_refactored_code()
    demonstrate_original_functionality()

    # Запуск тестов
    print("\n\n" + "=" * 60)
    print("ДЛЯ ЗАПУСКА ТЕСТОВ:")
    print("=" * 60)
    print("Выполните одну из следующих команд в терминале:")
    print("\n1. Запуск тестов через unittest:")
    print("   python -m unittest test_manufacturing.py")
    print("\n2. Запуск тестового файла напрямую:")
    print("   python test_manufacturing.py")
    print("\n3. Запуск с более подробным выводом:")
    print("   python -m unittest test_manufacturing.TestManufacturingService -v")
