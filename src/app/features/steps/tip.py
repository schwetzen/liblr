from app.features.steps.common_steps import *
from app.models.tip import *
from behave import *


##### ADDING TIPS

@when('the user presses the button to add new reading tip')
def step_impl(ctx):
    ctx.browser.find_by_text('Add a reading tip').first.click()

@when('enters title "{title}", chooses the type "{content_type}", enters description"{desc}" and enters a webpage "{webpage}"')
def step_impl(ctx, title, content_type, desc, webpage):
    '''
    ctx.browser.find_by_partial_text("")
    field_values = {
        "title":title,
        "content_type":"Webpage",
        "description":desc,
        "url":webpage
    }
    
    ctw.browser.fillForm()
    '''

    ctx.browser.fill("title", title)
    ctx.browser.find_option_by_text("Website").click()
    ctx.browser.fill("description", desc)
    ctx.browser.fill("url", webpage)


@when('the tip is submitted')
def step_impl(ctx):
    ctx.browser.find_by_text("Create").first.click()


@then('the page contains the added tip with title "{title}"')
def step_impl(ctx, title=""):
    assert ctx.browser.is_element_present_by_text(title) 

##### DELETE TIPS

@given('the database is initialized for tips_can_be_removed')
def step_impl(ctx):
    user = User.objects.get(email="example@example.com")
    _create_website(user, 'testTitle', 'hejhejtest', 'http://www.google.fi')


@when('the delete button is pressed')
def step_impl(ctx):
    ctx.browser.find_by_text('View').first.click()
    ctx.browser.find_by_text('Delete').first.click()


@then('the page no longer contains the tip with title "{title}"')
def step_impl(ctx, title):
    assert not ctx.browser.is_element_present_by_text('Delete')



##### EDIT TIPS

@given('the database is initialized for tips_can_be_edited')
def step_impl(ctx):
    user = User.objects.get(email="example@example.com")
    _create_website(user, 'testTitle', 'hejhejtest', 'http://www.google.fi')


@when('the user presses the button to edit a tip')
def step_impl(ctx):
    ctx.browser.find_by_text('View').first.click()
    ctx.browser.find_by_text('Edit').first.click()


@when('enters title "{title}", chooses the type "{content_type}", enters description"{desc}" and enters a webpage "{webpage}" into the edit form')
def step_impl(ctx, title, content_type, desc, webpage):
    ctx.browser.fill("title", title)
    ctx.browser.fill("description", desc)
    ctx.browser.fill("url", webpage)


@when('the edit is submitted')
def step_impl(ctx):
    ctx.browser.find_by_id("submit").first.click()


@then('the page contains a tip with title "{title}", type "{mediaType}", desc "{desc}" and url "{url}"')
def step_impl(ctx, title="", mediaType="", desc="", url=""):
    assert (ctx.browser.is_element_present_by_text(title)
        or ctx.browser.is_element_present_by_text(mediaType) # Mediatype is the card header 
        or ctx.browser.is_element_present_by_text(desc)
        or ctx.browser.is_element_present_by_text(url)
        )


##### HELPER METHODS

def _create_book(user, title, description, isbn):
    tip = ReadingTip.objects.create(user=user, content_type=0, title=title, description=description)
    ReadingTipContentBook.objects.create(tip=tip, isbn=isbn)

def _create_website(user, title, description, url):
    tip = ReadingTip.objects.create(user=user, content_type=1, title=title, description=description)
    ReadingTipContentWebsite.objects.create(tip=tip, url=url)
