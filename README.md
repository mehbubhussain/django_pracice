# django_pracice

Create virtual environment
pythone3 -m venv ./venv

Activate virtual environment
source ./venv/bin/activate

To Deactivate just run
deactivate
====================

To collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILE_DIR = [
    os.path.join(BASE_DIR, 'btre/static')
]

python manage.py collectstatic

=========================