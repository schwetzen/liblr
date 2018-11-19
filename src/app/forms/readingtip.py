from django.forms import ModelForm
from app.models import ReadingTip


class ReadingTipCreateForm(ModelForm):
    class Meta:
        model = ReadingTip
        fields = ['title', 'url', 'description']
