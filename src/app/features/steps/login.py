from app.features.steps.common_steps import *


@when('the user presses the login button')
def step_impl(ctx):
    ctx.browser.click_link_by_href('/login/')


@when('the user fills the login form with the username "{username}"')
def step_impl(ctx, username):
    ctx.browser.fill('username', username)
    ctx.browser.fill('password', DEFAULT_PASSWORD)
