from django import forms
from .models import Feature, EducationPost


#If you add a new feature later →The form updates automatically.

#No code modification needed.
class DiagnosisForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        features = Feature.objects.filter(is_active=True)

        for feature in features:
            self.fields[feature.name] = forms.IntegerField(
                label=feature.display_name,
                min_value=feature.min_value,
                max_value=feature.max_value,
                widget=forms.NumberInput(attrs={
                    "class": "form-control",
                    "placeholder": f"Enter value ({feature.min_value}-{feature.max_value})"
                })
            )


class EducationPostForm(forms.ModelForm):
    class Meta:
        model = EducationPost
        fields = ["title", "summary", "content", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title"}),
            "summary": forms.TextInput(attrs={"placeholder": "Short summary for patients"}),
            "content": forms.Textarea(attrs={"rows": 6, "placeholder": "Write educational guidance for patients"}),
        }
