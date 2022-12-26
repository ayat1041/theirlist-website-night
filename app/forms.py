from django import forms
from .models import Review,MusicReview,BookReview,Starr,MusicStarr,BookStarr

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'body')

#         widgets = {
#             'name' : forms.TextInput(),
#             'body' : forms.Textarea(),
#         }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "user",
            "List",
            "comment",
        ]
class MusicReviewForm(forms.ModelForm):
    class Meta:
        model = MusicReview
        fields = [
            "user",
            "MusicList",
            "comment",
        ]
class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = [
            "user",
            "BookList",
            "comment",
        ]

class StarrForm(forms.ModelForm):
    class Meta:
        model = Starr
        fields = [
            "user",
            "list",
            "rate",
        ]

class MusicStarrForm(forms.ModelForm):
    class Meta:
        model = MusicStarr
        fields = [
            "user",
            "list",
            "rate",
        ]

class BookStarrForm(forms.ModelForm):
    class Meta:
        model = BookStarr
        fields = [
            "user",
            "list",
            "rate",
        ]