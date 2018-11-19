from splinter.browser import Browser


def before_all(context):
    context.browser = Browser('firefox')


def after_all(context):
    context.browser.quit()
    context.browser = None
