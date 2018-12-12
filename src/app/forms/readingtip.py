from django import forms
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
from app.models import ReadingTip


class ReadingTipCreateForm(forms.ModelForm):
    class Meta:
        model = ReadingTip
        fields = ('title', 'content_type', 'description',)

    isbn = forms.CharField(
        label='ISBN',
        max_length=20,
        min_length=10,
        required=False,
    )

    url = forms.URLField(
        label='URL',
        max_length=255,
        required=False,
    )


class ReadingTipUpdateForm(forms.ModelForm):
    class Meta:
        model = ReadingTip
        fields = ('title', 'description',)

    start_date = forms.DateField(
        widget=SelectDateWidget(empty_label=('Year', 'Month', 'Day')),
        required=False
    )
    
    end_date = forms.DateField(
        widget=SelectDateWidget(empty_label=('Year', 'Month', 'Day')),
        required=False
    )

    isbn = forms.CharField(
        label='ISBN',
        max_length=20,
        min_length=10,
        required=False,
    )

    url = forms.URLField(
        label='URL',
        max_length=255,
        required=False,
    )
