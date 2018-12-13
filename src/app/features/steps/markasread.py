from app.features.steps.common_steps import *

@given('a tip is marked as read')
def step_impl(ctx):
    ctx.browser.find_by_text('Mark as read').first.click()

@given('a tip is marked as unread')
def step_impl(ctx):
    ctx.browser.find_by_text('Mark as unread').first.click()

@then('Then the page contains the text "Mark as unread"')
def step_impl(ctx):
    assert ctx.browser.is_element_present_by_text("Mark as unread")

@then('Then the page does not contain the text "Mark as unread"')
def step_impl(ctx):
    assert not ctx.browser.is_element_present_by_text("Mark as unread")
