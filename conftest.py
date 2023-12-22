import os
from datetime import datetime, timedelta

import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from smart_mingle_app.models import Event, ExtraDetails


@pytest.fixture(scope='session', autouse=True)
def configure_test_database():
    settings.DATABASES['default']['NAME'] = os.environ['TEST_DB_NAME']
    settings.DATABASES['default']['USER'] = os.environ['TEST_DB_USERNAME']
    settings.DATABASES['default']['PASSWORD'] = os.environ['TEST_DB_PASSWORD']
    settings.DATABASES['default']['HOST'] = os.environ['TEST_DB_HOST']
    settings.DATABASES['default']['PORT'] = os.environ['TEST_DB_PORT']
