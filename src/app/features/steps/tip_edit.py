from app.features.steps.common_steps import *
from app.features.steps.tip_utils import *


@given('the database is initialized for tips_can_be_edited')
def step_impl(ctx):
    user = User.objects.get(email="example@example.com")
    create_website(user, 'testTitle', 'hejhejtest', 'http://www.google.fi')


@when('the user presses the button to edit a tip')
def step_impl(ctx):
    ctx.browser.find_by_text('View').first.click()
    ctx.browser.find_by_text('Edit').first.click()


@when('enters title "{title}", enters description "{desc}" and enters url "{url}" into the edit form')
def step_impl(ctx, title, desc, url):
    ctx.browser.fill("title", title)
    ctx.browser.fill("description", desc)
    ctx.browser.fill("url", url)


@when('the edit form is submitted')
def step_impl(ctx):
    ctx.browser.find_by_id("submit").first.click()


@then('the page contains a tip with title "{title}", type "{content_type}", desc "{desc}" and url "{url}"')
def step_impl(ctx, title="", content_type="", desc="", url=""):
    assert (ctx.browser.is_element_present_by_text(title)
        or ctx.browser.is_element_present_by_text(content_type)
        or ctx.browser.is_element_present_by_text(desc)
        or ctx.browser.is_element_present_by_text(url)
        )

