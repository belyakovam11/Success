from __future__ import absolute_import, unicode_literals
# Эта строка гарантирует, что Celery будет загружаться при старте Django
from .celery_app import app as celery_app
__all__ = ('celery_app',)
