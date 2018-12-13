from app.features.steps.common_steps import *
from app.features.steps.tip_utils import *


@given('the database is initialized for tips_can_be_removed')
def step_impl(ctx):
    user = User.objects.get(email="example@example.com")
    create_website(user, 'testTitle', 'hejhejtest', 'http://www.google.fi')


@when('the delete button is pressed')
def step_impl(ctx):
    ctx.browser.find_by_text('View').first.click()
    ctx.browser.find_by_text('Delete').first.click()


@then('the page no longer contains the tip with title "{title}"')
def step_impl(ctx, title):
    assert not ctx.browser.is_element_present_by_text(title)
