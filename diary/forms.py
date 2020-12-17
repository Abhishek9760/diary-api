from django import forms

from .models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["user", "title", "text", "image"]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        text = data.get("text")
        if text == "":
            text = None
        image = data.get("image")
        if text is None and image is None:
            raise forms.ValidationError("Text or Image is required")
        return super().clean(*args, **kwargs)
