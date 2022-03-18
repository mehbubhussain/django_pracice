# django_pracice

Create virtual environment
python3 -m venv ./venv

Activate virtual environment
source ./venv/bin/activate

python manage.py rubserver to start the application

To Deactivate just run
deactivate
====================

To collectstatic

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]

python manage.py collectstatic

=========================
