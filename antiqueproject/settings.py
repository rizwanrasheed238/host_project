"""
Django settings for antiqueproject project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^a6qz_i!)e2m)tq2_%rcbv*irxsp8c&j2_klt%m4()3&84lhck'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'admin_interface',
    # 'colorfield',
    'antiqueapp',
    'jazzmin',
    'cart',
    'seller',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'antiqueproject.urls'

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
                # 'antiqueapp.context_processors.menu_links',

            ],
        },
    },
]

WSGI_APPLICATION = 'antiqueproject.wsgi.application'
AUTH_USER_MODEL='antiqueapp.Account'

# Databaser
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR /'db.sqlite3',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME':'antiquestore',
        # 'USER':'root',
        # 'PASSWORD':'',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'medievalstore123@gmail.com'
DEFAULT_FROM_EMAIL = 'medievalstore123@gmail.com'
SERVER_EMAIL = 'medievalstore123@gmail.com'
EMAIL_HOST_PASSWORD = 'fdekeztlpmzwqxru'

EMAIL_USE_TLS = True

RAZORPAY_API_KEY = 'rzp_test_nxdXNnVaXveQ3g'
RAZORPAY_API_SECRET_KEY = 'oOj7ibAw4djaYiT4PZUy5W8y'


JAZZMIN_SETTINGS = {


    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Shop",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "assets/images/demos/demo-2/logo.png",


    # Links to put along the top menu
    "topmenu_links": [


        # external url that opens in a new window (Permissions can be added)
        {"name": "View Website", "url": "http://127.0.0.1:8000/", "new_window": True},
        {"name": "Sales Chart", "url": "http://127.0.0.1:8000/view/", "new_window": True},
        {"name":"Sentiment Graph", "url":"http://127.0.0.1:8000/admin/antiqueapp/product/sentiment-graph/","new_window":True},
        {"name":"Product Sales", "url":"http://127.0.0.1:8000/admin/antiqueapp/product/top-products/","new_window":True},


    ],
    #
    # #############
    # # User Menu #
    # #############
    #
    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Contact", "url": "https://github.com/rizwanrasheeed238", "new_window": True},
        {"model": "auth.user"}
    ],


    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    #
    # # Custom links to append to app groups, keyed on app names
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },
    #
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    # "icons": {
    #     "auth": "fas fa-users-cog",
    #     "auth.user": "fas fa-user",
    #     "auth.Group": "fas fa-users",
    # },
    # # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-chevron-circle-right",
    # "default_icon_children": "fas fa-circle",
    #
    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    # "related_modal_active": False,
    #
    # #############
    # # UI Tweaks #
    # ############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": "css/app.css",
    # "custom_js": "js/vendor.js",
    #
    # # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    # "use_google_fonts_cdn": True,
    # # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    # "changeform_format": "horizontal_tabs",
    # # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

}
JAZZMIN_UI_TWEAKS = {
     "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "dark_mode_theme": "superhero",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

