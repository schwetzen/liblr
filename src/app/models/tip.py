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
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    has_been_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def readable_type(self):
        _, value = ReadingTip.CONTENT_TYPE[self.content_type]
        return value

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

    def export_fields(self):
        return (
            self.readable_type(),
            self.title,
            self.content().isbn if hasattr(self.content(), 'isbn') else '',
            self.content().url if hasattr(self.content(), 'url') else '',
            self.description,
        )


class ReadingTipContentBook(models.Model):
    class Meta:
        get_latest_by = ('id',)

    tip = models.ForeignKey(
        'ReadingTip',
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField(max_length=50)


class ReadingTipContentWebsite(models.Model):
    class Meta:
        get_latest_by = ('id',)

    tip = models.ForeignKey(
        'ReadingTip',
        on_delete=models.CASCADE,
        related_name='websites'
    )
    url = models.URLField()
