import django
from django_nose.runner import NoseTestSuiteRunner

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "account.test.settings")

django.setup()
test_runner = NoseTestSuiteRunner()

failures = test_runner.run_tests(['account'])
if failures:
    sys.exit(failures)
