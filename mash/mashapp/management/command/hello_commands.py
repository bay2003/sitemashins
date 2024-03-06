from django.core.management.base import BaseCommand
from django.conf import settings
import os
class Command(BaseCommand):
    # def handle(self, *args, **options):
    #     path = os.path.join(serrings.BASE_DIR, 'mashapp', 'management', 'command', 'file_save', 'file.json')
    #     with open(path, 'w') as f:
    #         pass

        print("Hello")