from splinter.browser import Browser
from django.core.management import call_command


def before_all(context):
    context.browser = Browser('chrome', headless=False)


def after_all(context):
    context.browser.quit()
    context.browser = None


def before_scenario(context, scenario):
    call_command('flush', verbosity=0, interactive=False)
