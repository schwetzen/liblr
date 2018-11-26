from django.db import models


class ReadingTip(models.Model):
    BOOK = 0
    WEBSITE = 1

    CONTENT_TYPE = (
        (BOOK, 'Book'),
        (WEBSITE, 'Website'),
    )

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reading_tips'
    )
    content_type = models.IntegerField(choices=CONTENT_TYPE)
    title = models.CharField(verbose_name='Title', max_length=30)
    description = models.TextField(verbose_name='Description', blank=True)
    has_been_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def content(self):
        if self.content_type == ReadingTip.BOOK:
            try:
                return self.books.latest()
            except ReadingTipContentBook.DoesNotExist:
                return None

        if self.content_type == ReadingTip.WEBSITE:
            try:
                return self.websites.latest()
            except ReadingTipContentWebsite.DoesNotExist:
                return None


class ReadingTipContentWebsite(models.Model):
    class Meta:
        get_latest_by = ('-id',)

    tip = models.ForeignKey(
        'ReadingTip',
        on_delete=models.CASCADE,
        related_name='websites'
    )
    url = models.URLField()


class ReadingTipContentBook(models.Model):
    class Meta:
        get_latest_by = ('-id',)

    tip = models.ForeignKey(
        'ReadingTip',
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField(max_length=50)
