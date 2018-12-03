from app.features.steps.common_steps import *


@when('the user presses the logout button')
def step_impl(ctx):
    ctx.browser.find_by_name('logout').first.click()


@then('the page contains the login link')
def step_impl(ctx):
    assert len(ctx.browser.find_link_by_href('/login/')) == 1
