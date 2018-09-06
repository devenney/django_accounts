DEBUG=True
SECRET_KEY = 'TEST_ONLY_NO_PROD' # noqa

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF='accounts.urls'

INSTALLED_APPS=(
    'accounts',

    'django_nose',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'registration',
    'two_factor',
    'widget_tweaks',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django_otp.middleware.OTPMiddleware', # Django 2FA
    'two_factor.middleware.threadlocals.ThreadLocals', # Twilio Gateway

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEST_RUNNER="django_nose.NoseTestSuiteRunner"

# Django Registration
ACTIVATION_EMAIL_HTML='email/activation.html'
PASSWORD_RESET_EMAIL_HTML='email/password_reset.html'

# Django 2FA
LOGIN_URL = 'auth_login'
LOGIN_REDIRECT_URL = 'account_settings'
