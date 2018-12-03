from behave import *
from app.models.user import User
from django.db.models import Q


DEFAULT_PASSWORD = 'zxcvbnm,.'


def rel_url(context, url=""):
    return context.config.server_url + url


@given('a user account with the email "{email}" exists')
def step_impl(ctx, email):
    user = User.objects.filter(Q(email=email)).first()
    if not user:
        User.objects.create_user(email=email, password=DEFAULT_PASSWORD)


@given('a user account with the email "{email}" does not exist')
def step_impl(ctx, email):
    user = User.objects.filter(Q(email=email)).first()
    if user:
        user.delete()


@given('the user is logged out')
def step_impl(ctx):
    ctx.browser.visit(rel_url(ctx, '/logout/'))


@given('the user "{username}" is logged in')
def step_impl(ctx, username):
    ctx.browser.visit(rel_url(ctx, '/login/'))
    ctx.browser.fill('username', username)
    ctx.browser.fill('password', DEFAULT_PASSWORD)
    ctx.browser.find_by_name('submit').first.click()


@given('the url is "{url}"')
def step_impl(ctx, url=""):
    ctx.browser.visit(rel_url(ctx, url))


@when('the form is submitted')
def step_impl(ctx):
    ctx.browser.find_by_name('submit').first.click()


@then('the url is "{url}"')
def step_impl(ctx, url):
    assert ctx.browser.url == rel_url(ctx, url)


@then('a user account with the email "{email}" exists')
def step_impl(ctx, email):
    assert len(User.objects.filter(Q(email=email))) == 1
