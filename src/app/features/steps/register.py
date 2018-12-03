from app.features.steps.common_steps import *


@when('the user presses register button')
def step_impl(ctx):
    ctx.browser.click_link_by_href('/register/')


@when('the user fills the register form with the email "{email}"')
def step_impl(ctx, email):
    ctx.browser.fill('email', email)
    ctx.browser.fill('password1', DEFAULT_PASSWORD)
    ctx.browser.fill('password2', DEFAULT_PASSWORD)
