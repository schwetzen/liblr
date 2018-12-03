from behave import *


def rel_url(context, url=""):
    return context.config.server_url + url


@given('the url is "{url}"')
def step_impl(ctx, url=""):
    ctx.browser.visit(rel_url(ctx, url))


@then('the url is "{url}"')
def step_impl(ctx, url):
    assert ctx.browser.url == rel_url(ctx, url)
