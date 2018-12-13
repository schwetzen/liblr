from app.features.steps.common_steps import *
from app.features.steps.tip_utils import *
from behave import *


@given('the database is initialized for tips_can_be_searched')
def step_impl(ctx):
    user = User.objects.get(email="example@example.com")
    create_website(user, 'Google', 'This is a link to google', 'http://www.google.fi')
    create_website(user, 'Youtube', 'This is a link to youtube', 'http://www.youtube.com')


@when('the user enters the search term "{term}"')
def step_impl(ctx, term):
    ctx.browser.fill("search", term)


@when('presses the search button')
def step_impl(ctx):
    ctx.browser.find_by_xpath('/html/body/nav/div/div[1]/form/div/span/button').click()


@then('the user will be presented with tips including keyword "{keyword}"')
def step_impl(ctx, keyword):
    assert (ctx.browser.is_element_present_by_text(keyword)
            and len(ctx.browser.find_by_text(keyword)) == 1
            )
