from django import forms
from .models import Post, Comment, User, Location, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['location'].required = False
        self.fields['category'].required = False

        self.fields['location'].queryset = (
            Location.objects.all().order_by('name'))
        self.fields['category'].queryset = (
            Category.objects.all().order_by('title'))

        self.fields['location'].empty_label = "Выберите местоположение"
        self.fields['category'].empty_label = "Выберите категорию"

        self.fields['pub_date'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}
        )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
