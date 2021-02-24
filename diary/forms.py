from django import forms

from .models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["user", "title", "text", "image"]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        text = data.get("text")
        title = data.get("title")
        if not(title and text):
            raise forms.ValidationError("title and text is required")
        return super().clean(*args, **kwargs)
