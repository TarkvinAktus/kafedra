from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment,UserProfileInfo, Course, StudyDoc, Diploma, LabInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
    


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name',)
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
        }


class StudyDocForm(forms.ModelForm):
    class Meta:
        model = StudyDoc
        fields = ('name', 'document' ,'course')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'document':forms.ClearableFileInput(attrs={'multiple': False}),
            'course':forms.Select(choices=Course.objects.all().values_list('name',)),
        }


class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ('theme', 'student' ,'teacher')

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'textinputclass'}),
            'student': forms.TextInput(attrs={'class': 'textinputclass'}),
            'teacher': forms.TextInput(attrs={'class': 'textinputclass'}),
        }


class LabInfo(forms.ModelForm):
    class Meta:
        model = LabInfo
        fields = '__all__'
