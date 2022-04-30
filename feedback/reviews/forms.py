from django import forms
from .models import Review

class ReviewForm1(forms.Form):
    user_name = forms.CharField(label="User_Name",max_length=50,min_length=5,required=True,error_messages={
        "required" : "User_Name must not be empty.",
        "min_length" : "User_Name mush have atleast 5 characters.",
        "max_length" : "User_Name mush not be greater than 50 characters."
    })

    review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200,required=True,error_messages={
        "required" : "Feedback must not be empty.",
        "max_length" : "Feedback mush not be greater than 200 characters."
    })

    rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=10,required=True,error_messages={
        "required" : "Rating must not be empty.",
        "min_value" : "Rating must not be less than 1.",
        "max_value" : "Rating must not be greater than 10."
    })

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #fields = ['user_name','review_text','rating']
        fields = '__all__'
        #exclude = ['owner_comment']
        labels = {
            'user_name' : 'User Name',
            'review_text' : 'Your Feedback',
            'rating' : 'Your Rating'
        }
        error_messages = {
            'user_name':{
                "required" : "User_Name must not be empty.",
                "min_length" : "User_Name mush have atleast 5 characters.",
                "max_length" : "User_Name mush not be greater than 50 characters."
            },
            'review_text':{
                "required" : "Feedback must not be empty.",
                "max_length" : "Feedback mush not be greater than 200 characters."
            },
            'rating':{
                "required" : "Rating must not be empty.",
                "min_value" : "Rating must not be less than 1.",
                "max_value" : "Rating must not be greater than 10."
            }
        }
