import django.test
from django.core.exceptions import ValidationError
from app.models.tip import ReadingTip


class ReadingTipTestCase(django.test.SimpleTestCase):

    def _initialize(self):
        self.test_title = 'Test title'
        self.test_url = 'google.com'
        self.test_desc = 'Testing'

    def _create_instance(self, title=None, url=None, desc=None):
        self._initialize()
        if title is None:
            title = self.test_title
        if url is None:
            url = self.test_url
        if desc is None:
            desc = self.test_desc
        return ReadingTip(title=title, url=url, description=desc)

    def test_arguments_normal(self):
        tip = self._create_instance()
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError unexpectedly!')

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
            self.fail('ReadingTip.clean_fields() raised a ValidationError unexpectedly!')

    def test_url_too_long(self):
        limit = 21
        long_url = 'a' * limit
        tip = self._create_instance(url=long_url)
        self.assertRaises(ValidationError, tip.clean_fields)

    def test_desc_blank(self):
        tip = self._create_instance(desc='')
        try:
            tip.clean_fields()
        except ValidationError:
            self.fail('ReadingTip.clean_fields() raised a ValidationError unexpectedly!')
