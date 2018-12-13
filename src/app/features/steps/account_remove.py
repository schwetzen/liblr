from app.features.steps.common_steps import *

@when('the user confirms this decision')
def step_impl(ctx):
    ctx.browser.find_by_text("Delete").first.click()

@when('the user presses the button to delete the account')
def step_impl(ctx):
    ctx.browser.visit(rel_url(ctx, "/settings/delete/"))

@when('the url is "/login/"')
def step_impl(ctx):
    ctx.browser.visit(rel_url(ctx, "/login/"))
