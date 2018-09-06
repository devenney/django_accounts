import coverage
import django
from django_nose.runner import NoseTestSuiteRunner

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accounts.test.settings")

    cov = coverage.coverage(
        source=['accounts'],
        omit=['*/migrations/*', '*/test/*'],
    )
    cov.erase()
    cov.start()

    django.setup()
    test_runner = NoseTestSuiteRunner()

    failures = test_runner.run_tests(['accounts'])

    cov.stop()
    cov.save()
    cov.report()

    if failures:
        sys.exit(failures)
