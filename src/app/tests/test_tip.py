from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models import ReadingTip, User


USER = None
CONTENT_TYPE = ReadingTip.BOOK
TITLE = 'Test title'
URL = 'https://google.com'
DESCRIPTION = 'Lorem ipsum dolor sit amet.'


class ReadingTipTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        global USER
        USER = User.objects.create_user('example@example.com', 'qwerty123')

    @staticmethod
    def _create_instance(content_type=None, title=None, description=None):
        return ReadingTip(
            user=USER,
            content_type=content_type if content_type is not None else CONTENT_TYPE,
            title=title if title is not None else TITLE,
            description=description if description is not None else DESCRIPTION
        )

    def test_arguments_normal(self):
        tip = ReadingTipTestCase._create_instance()
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError.')

    def test_title_blank(self):
        tip = ReadingTipTestCase._create_instance(title='')
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_title_too_long(self):
        limit = 31
        long_title = 'a' * limit
        tip = ReadingTipTestCase._create_instance(title=long_title)
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_desc_blank(self):
        tip = ReadingTipTestCase._create_instance(description='')
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError.')
