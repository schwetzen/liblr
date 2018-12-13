from app.features.steps.common_steps import *
from datetime import datetime

@when('the user selects the calendar view from the navbar')
def step_impl(ctx):
    ctx.browser.find_by_text('Calendar').first.click()

@when('sets the start and end dates')
def step_impl(ctx):
    day = datetime.now().strftime('%d')
    month = datetime.now().strftime('%B')
    year = datetime.now().strftime('%Y')
    ctx.browser.find_option_by_text(day).click()
    ctx.browser.find_option_by_text(month).click()
    ctx.browser.find_option_by_text(year).click()

@then('the page contains a button called "today"')
def step_impl(ctx):
    assert ctx.browser.is_element_present_by_text("today")