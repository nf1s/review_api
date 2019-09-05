from django.forms.models import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["product", "comment", "stars"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "UPDATE"))
