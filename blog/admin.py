from django.contrib import admin

from .models import Post, Comment, UserProfileInfo, Course, StudyDoc, Diploma, LabInfo, Lab

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)
admin.site.register(Course)
admin.site.register(StudyDoc)
admin.site.register(Diploma)
admin.site.register(LabInfo)
admin.site.register(Lab)