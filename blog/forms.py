from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment,UserProfileInfo, Course, StudyDoc, Diploma, LabInfo, Lab

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'multiple': False,'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'multiple': False,'class': 'form-control'}),
        }

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

        widgets = {
            'portfolio_site': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic':forms.FileInput(attrs={'multiple': False,'class': 'custom-file-input'}),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
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
            'theme': forms.TextInput(attrs={'type':'text','class': 'form-control','id':'theme'}),
            'student': forms.TextInput(attrs={'class': 'form-control','id':'student'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LabInfo(forms.ModelForm):
    class Meta:
        model = LabInfo
        fields = '__all__'

class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('student','lab')

