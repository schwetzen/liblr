from app.features.steps.common_steps import *


@when('the user presses the button to add new reading tip')
def step_impl(ctx):
    ctx.browser.find_by_text('Add a reading tip').first.click()


@when('the Website creation form is filled with the title "{title}", description "{desc}" and url "{url}"')
def step_impl(ctx, title, desc, url):
    ctx.browser.fill("title", title)
    ctx.browser.find_option_by_text("Website").click()
    ctx.browser.fill("description", desc)
    ctx.browser.fill("url", url)

@when('the Book creation form is filled with the title "{title}", description "{desc}" and isbn "{isbn}"')
def step_impl(ctx, title, desc, isbn):
    ctx.browser.fill("title", title)
    ctx.browser.find_option_by_text("Book").click()
    ctx.browser.fill("description", desc)
    ctx.browser.fill("isbn", isbn)

@when('the tip is submitted')
def step_impl(ctx):
    ctx.browser.find_by_text("Create").first.click()


@then('the page contains the added tip with title "{title}"')
def step_impl(ctx, title=""):
    assert ctx.browser.is_element_present_by_text(title)
