from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=100, error_messages={
        "required": "Your username must not be empty",
        "max_length": "Please enter a shorter username"
    })
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=2000)
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)
    