from django import forms
from .models import Feature


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
