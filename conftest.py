# conftest.py
import os
import pytest
from func import *  # импортируем твою функцию

# фикстура запускается перед каждым тестом, если в воркфлоу указаны параметры задержки
# @pytest.fixture(autouse=True)
# def apply_lucky_sleep_conditionally():
#     """
#     Выполняется только если заданы переменные окружения LUCKY_SLEEP_MIN и LUCKY_SLEEP_MAX.
#     """
#     min_env = os.getenv("LUCKY_SLEEP_MIN")
#     max_env = os.getenv("LUCKY_SLEEP_MAX")
#
#     # Если хотя бы одна из переменных не задана, фикстура пропускается
#     if min_env is None or max_env is None:
#         return
#
#     # Преобразуем в int
#     min_seconds = int(min_env)
#     max_seconds = int(max_env)
#
#     lucky_sleep(min_seconds, max_seconds)

# хук который запускается прямо внутри теста если в воркфлоу е сть параметры
# два параметра, чтобы замедлить выполнение тестов
# LUCKY_SLEEP_MIN: 10
# LUCKY_SLEEP_MAX: 100
def pytest_runtest_call(item):
    """
    Хук выполняется **внутри каждого теста**, перед его основной логикой.
    """
    min_env = os.getenv("LUCKY_SLEEP_MIN")
    max_env = os.getenv("LUCKY_SLEEP_MAX")

    if min_env is None or max_env is None:
        return  # ничего не делаем, тест выполняется сразу

    min_seconds = int(min_env)
    max_seconds = int(max_env)

    lucky_sleep(min_seconds, max_seconds)  # тест реально ждёт здесь