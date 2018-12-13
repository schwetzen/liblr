from app.features.steps.common_steps import *


@when('the user presses the button to add new reading tip')
def step_impl(ctx):
    ctx.browser.find_by_text('Add a reading tip').first.click()


@when('enters title "{title}", selects Website, enters description "{desc}" and enters url "{url}"')
def step_impl(ctx, title, desc, url):
    ctx.browser.fill("title", title)
    ctx.browser.find_option_by_text("Website").click()
    ctx.browser.fill("description", desc)
    ctx.browser.fill("url", url)


@when('the tip is submitted')
def step_impl(ctx):
    ctx.browser.find_by_text("Create").first.click()


@then('the page contains the added tip with title "{title}"')
def step_impl(ctx, title=""):
    assert ctx.browser.is_element_present_by_text(title)
