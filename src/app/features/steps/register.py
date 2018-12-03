from app.features.steps.common_steps import *
from app.models.user import User
from django.db.models import Q


@when('the user presses register button')
def step_impl(ctx):
    ctx.browser.click_link_by_href('/register/')


@when('the user fills the form with the email "{email}"')
def step_impl(ctx, email):
    ctx.browser.fill('email', email)
    ctx.browser.fill('password1', 'zxcvbnm,.')
    ctx.browser.fill('password2', 'zxcvbnm,.')


@then('a user account with the email "{email}" exists')
def step_impl(ctx, email):
    assert len(User.objects.filter(Q(email=email))) == 1
