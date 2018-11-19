from django import forms
from app.models import ReadingTip


class ReadingTipCreateForm(forms.ModelForm):
    class Meta:
        model = ReadingTip
        fields = ('title', 'url', 'description',)
