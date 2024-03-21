import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

# Установка переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mash.settings")

# Вызов функции django.setup()
django.setup()

# Импорт моделей Django
from usersapp.models import BlogUser
from mashapp.models import Project, Category, Tag, Post, Create

# Загрузка тестового класса
TestRunner = get_runner(settings)
test_runner = TestRunner()

# Исполнение тестов
failures = test_runner.run_tests(["mashapp"])

# Возврат кода выхода
sys.exit(bool(failures))

