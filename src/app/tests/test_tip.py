from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models import ReadingTip


TITLE = 'Test title'
URL = 'https://google.com'
DESCRIPTION = 'Lorem ipsum dolor sit amet.'


class ReadingTipTestCase(TestCase):

    def _create_instance(self, title=None, url=None, description=None):
        return ReadingTip(
            title=title if title is not None else TITLE,
            url=url if url is not None else URL,
            description=description if description is not None else DESCRIPTION
        )

    def test_arguments_normal(self):
        tip = self._create_instance()
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError.')

    def test_title_blank(self):
        tip = self._create_instance(title='')
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_title_too_long(self):
        limit = 31
        long_title = 'a' * limit
        tip = self._create_instance(title=long_title)
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_url_blank(self):
        tip = self._create_instance(url='')
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError.')

    def test_url_too_long(self):
        limit = 21
        long_url = 'a' * limit
        tip = self._create_instance(url=long_url)
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_desc_blank(self):
        tip = self._create_instance(description='')
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError.')
