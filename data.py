class URLs:
    """Класс для хранения URL страниц"""
    BASE = "https://stellarburgers.education-services.ru"
    MAIN = BASE + "/"                                # Главная страница
    LOGIN = BASE + "/login"                          # Страница входа
    REGISTER = BASE + "/register"                    # Страница регистрации
    FORGOT_PASSWORD = BASE + "/forgot-password"      # Восстановление пароля
    PROFILE = BASE + "/account/profile"              # Личный кабинет
    ORDER_HISTORY = BASE + "/account/order-history"  # История заказов

class Credentials:
    """Учетные данные зарегистрированного пользователя"""
    EMAIL = "Olga_32_132@yandex.ru"
    PASSWORD = "qwerty1234"

class TextMessages:
    """Текстовые элементы приложения"""
    PASSWORD_ERROR = "Некорректный пароль"   # Ошибка валидации пароля
    LOGIN_BUTTON = "Войти"                   # Текст кнопки входа
    REGISTER_BUTTON = "Зарегистрироваться"   # Текст кнопки регистрации

    # Разделы конструктора
    BUNS = "Булки"
    SAUCES = "Соусы"
    FILLINGS = "Начинки"


class Settings:
    """Настройки приложения"""
    WINDOW_WIDTH = 1366       # Ширина окна браузера
    WINDOW_HEIGHT = 768       # Высота окна браузера
    DEFAULT_TIMEOUT = 10      # Стандартное время ожидания
    MIN_PASSWORD_LENGTH = 6   # Минимальная длина пароля


# Номер когорты для генерации email
COHORT = "32"