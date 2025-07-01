from django import forms

class GeneratePostsForm(forms.Form):
    strategy_id = forms.IntegerField(label="Strategy Request ID")
    number_of_posts = forms.IntegerField(label="Number of Posts", initial=12)
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
