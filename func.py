import random
import pytest
import time

def lucky_step(chance: float = 0.6) -> None:
    """
    С вероятностью `chance` ломает тест.
    Возможные исходы с весами:
      - Failed (pytest.fail) 50%
      - Broken (ValueError, TypeError, KeyError) 30%
      - Skipped (pytest.skip) 20%
    Сообщения выбираются случайно из расширенных списков.
    """
    if not 0 <= chance <= 1:
        raise ValueError("Параметр 'chance' должен быть в диапазоне от 0 до 1")

    if random.random() < chance:
        outcome = random.choices(
            ["failed", "broken", "skipped"],
            weights=[50, 30, 20],
            k=1
        )[0]

        # Расширенные осмысленные сообщения
        failed_messages = [
            "инфраструктурная ошибка",
            "проверка данных не прошла",
            "обнаружено несоответствие результата ожидаемому",
            "результат не совпадает с эталоном",
            "проверка элементов страницы не удалась",
            "значение переменной не соответствует ожиданиям"
        ]

        broken_messages = [
            "некорректное значение в тесте",
            "тип данных не совпадает с ожидаемым",
            "ключ не найден в словаре",
            "Ошибка выполнения шага теста",
            "Необработанное исключение во время теста",
            "runtime exception, тест не удалось корректно завершить"
        ]

        skipped_messages = [
            "условие для выполнения шага не выполнено",
            "тестовый шаг был проигнорирован",
            "зависимость теста отсутствует или не активна",
            "данные для проверки недоступны",
            "выполнение шага временно отключено",
            "тест не применим для текущей конфигурации"
        ]

        if outcome == "failed":
            pytest.fail(random.choice(failed_messages))
        elif outcome == "broken":
            error_type = random.choice([ValueError, TypeError, KeyError])
            raise error_type(random.choice(broken_messages))
        elif outcome == "skipped":
            pytest.skip(random.choice(skipped_messages))
        else:
            pass

def lucky_sleep(min_seconds: int = 10, max_seconds: int = 100) -> None:
    """
    Задержка выполнения теста на случайное время в диапазоне [min_seconds, max_seconds].
    По умолчанию от 10 до 100 секунд.
    """
    if min_seconds < 0 or max_seconds < min_seconds:
        raise ValueError("Некорректные параметры задержки")

    delay = random.randint(min_seconds, max_seconds)
    print(f"[lucky_sleep] Тест ждет {delay} секунд...")
    time.sleep(delay)