from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofileinfo')

    #about = models.TextField()
    #additional
    diploma_count = models.IntegerField(default = 0)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='MEDIA_URL/profile_pics/',blank=True)


    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey('blog.UserProfileInfo', related_name='teachercourse',on_delete=models.CASCADE)
    url = models.URLField(blank=True)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users")


def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = 'courses/{course_dir}/{filename}'.format(
         course_dir=instance.course, filename=filename) 
    
    print(file_path)
    return file_path


class StudyDoc(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey('blog.Course', related_name='course',on_delete=models.CASCADE,null=True,blank=True)
    teacher = models.ForeignKey('blog.UserProfileInfo', related_name='teacherdoc',on_delete=models.CASCADE)
    document = models.FileField(upload_to=content_file_name)
    common = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users",kwargs={'pk':self.pk})


class Diploma(models.Model):
    theme = models.CharField(max_length=200)
    student = models.ForeignKey('blog.UserProfileInfo', related_name='studentdiploma',null=True,on_delete=models.SET_NULL)
    teacher = models.ForeignKey('blog.UserProfileInfo', related_name='teacherdiploma',null=True,on_delete=models.SET_NULL)


class Lab(models.Model):
    student = models.ForeignKey('blog.UserProfileInfo', unique=False,related_name='labinfo',on_delete=models.CASCADE)
    lab = models.ForeignKey('blog.LabInfo', related_name='labinfoname',on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approve_date = models.DateTimeField(blank=True, null=True)
    real_approve_date = models.DateTimeField(blank=True, null=True)


class LabInfo(models.Model):
    course = models.ForeignKey('blog.Course', related_name='lablist',null=True,on_delete=models.CASCADE)
    lab_name = models.CharField(max_length=20)
    lab_number = models.IntegerField(default = 0)
    link1 = models.URLField(blank=True)
    link2 =  models.URLField(blank=True)

    def __str__(self):
        return str(self.lab_number) + '.' + self.lab_name

    def get_absolute_url(self):
        return reverse("labinfo_detail",kwargs={'pk':self.pk})
