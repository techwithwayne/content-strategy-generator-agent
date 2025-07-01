from django import forms

class GeneratePostsForm(forms.Form):
    strategy_id = forms.IntegerField(label="Strategy Request ID")
    number_of_posts = forms.IntegerField(label="Number of Posts", initial=12)
