from django.urls import re_path,path
from blog import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('registration/',views.register,name='register'),
    path('about/',views.AboutView.as_view(),name='about'),

    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    

    path('addCourse/', views.AddCourseView.as_view(), name='addCourse'),
    path('tCourses/user/<int:pk>', views.TeacherCourseListView.as_view(), name='tCourses'),
    
    path('tCourses/<int:pk>/new_lab', views.LabInfoCreateView.as_view(), name='new_lab'),
    path('tCourses/<int:pk>', views.LabInfoListView.as_view(), name='labs'),
    path('course/<int:course>/lab/<int:pk>/delete', views.LabInfoDeleteView.as_view(), name='labdel'),
    path('lab/<int:pk>', views.LabInfoDetailView.as_view(), name='labdet'),
    
    
    re_path(r'^(?P<user>[-\w]+)/(?P<course>[-\w]+)/$',views.StudyDocList.as_view(),name='docs'),
    path('newdoc/user/<int:pk>', views.CreateStudyDocView.as_view(), name='newdoc'),
    path('newCommonDoc/<int:pk>', views.CreateStudyDocCommonView.as_view(), name='newdoccommon'),
    path('AllCommonDoc', views.StudyDocCommonView.as_view(), name='allcommon'),
    path('deldoc/<int:pk>',views.StudyDocDeleteView.as_view(), name='deldoc'),
    path('doc_detail/<int:pk>',views.StudyDocDetailView.as_view(), name='docdet'),

    path('newdiploma',views.DiplomaCreateView.as_view(), name='newdiploma'),
    path('diploma_list/teacher/<int:pk>',views.DiplomaList.as_view(), name='diploma_list'),


    re_path(r'lab_table/(?P<course>[\w\-]+)',views.LabAllStudentsList.as_view(), name='lab_table'),
    path('lab_detail/<int:pk>',views.LabDetailView.as_view(), name='lab_detail'),
    path('lab_update/<int:pk>',views.approve_lab, name='update_lab'),
    re_path(r'lab_journal_new/(?P<course>[\w\-]+)',views.LabCreateView.as_view(), name='new_lab_journal'),
        

    path('users/>', views.UsersList.as_view(), name='users'),
    path('students/>', views.StudentsList.as_view(), name='students'),
    path('g_students/>', views.GroupsStudentsList.as_view(), name='g_students'),
    path('t_students/>', views.TableStudentsList.as_view(), name='t_students'),
    path('user/<int:pk>', views.UserProfileInfoDetail.as_view(), name='user_detail'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)