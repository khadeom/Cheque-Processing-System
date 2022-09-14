

# from settings import get_BASE_DIR
import os, django
# os.environ['DJANGO_SETTINGS_MODULE'] = '../core.settings'
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".core.settings")
# django.setup()

# from django.conf import settings
# baseDir= settings.get_BASE_DIR()

baseDir=os.getcwd()
baseDir=os.path.dirname(__file__)
print(baseDir)

from pathlib import Path

p= Path(os.path.abspath(__file__)).parents[2]

print(p)