from django import forms

DISPLAY_CHOICES = (
    ("mode1", "Mode 1"),
    ("mode2", "Mode 2")
)


class DisplayType(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)
