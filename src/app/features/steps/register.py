from app.features.steps.common_steps import *


@when('user presses register button')
def step_impl(ctx):
    ctx.browser.click_link_by_href('/register/')


@when('user fills out and submits the register form')
def step_impl(ctx):
    ctx.browser.fill('email', 'example@example.com')
    ctx.browser.fill('password1', 'zxcvbnm,.')
    ctx.browser.fill('password2', 'zxcvbnm,.')
    ctx.browser.find_by_name('submit').first.click()
