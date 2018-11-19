from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@when('we implement another test')
def step_impl(context):
    assert False is not True


@then('behave will test it for us')
def step_impl(context):
    assert context.failed is False
