from behave import given, when, then


def rel_url(context, url=""):
    return context.config.server_url + url


@given('user is at home page')
def step_impl(ctx):
    ctx.browser.visit(rel_url(ctx))


@when('user presses register button')
def step_impl(ctx):
    ctx.browser.click_link_by_href('/register/')


@then('user is redirected to register page')
def step_impl(ctx):
    assert ctx.browser.url == rel_url(ctx, '/register/')


@given('user is at register page')
def step_impl(ctx):
    ctx.browser.visit(rel_url(ctx, '/register/'))


@when('user fills out and submits the register form')
def step_impl(ctx):
    ctx.browser.fill('email', 'example@example.com')
    ctx.browser.fill('password1', 'zxcvbnm,.')
    ctx.browser.fill('password2', 'zxcvbnm,.')
    ctx.browser.find_by_name('submit').first.click()


@then('a new user is registered')
def step_impl(ctx):
    assert ctx.browser.url == rel_url(ctx, '/login/')
