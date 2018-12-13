from app.models.tip import *


def create_book(user, title, description, isbn):
    tip = ReadingTip.objects.create(user=user, content_type=0, title=title, description=description)
    ReadingTipContentBook.objects.create(tip=tip, isbn=isbn)


def create_website(user, title, description, url):
    tip = ReadingTip.objects.create(user=user, content_type=1, title=title, description=description)
    ReadingTipContentWebsite.objects.create(tip=tip, url=url)
