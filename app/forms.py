from django import forms
from .models import Feedback,Review,MusicReview,BookReview,Starr,MusicStarr,BookStarr,Profile

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

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "user",
            "subject",
            "detail",
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio",
            #"location",
            #"birth_date",
            #"profile_pic",
            "fav_music_genre",
            "fav_Book_genre",
            "fav_movie_genre",
        ]