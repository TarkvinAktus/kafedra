from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from blog.models import (User, Post, Comment, UserProfileInfo, 
                        Course, StudyDoc, Diploma, LabInfo, Lab)
from django.utils import timezone
from django.db.models import Q
from blog.forms import (PostForm, CommentForm, 
                        UserForm, UserProfileInfoForm, 
                        CourseForm ,StudyDocForm, DiplomaForm)
import os
from django.conf import settings

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    


class UserProfileInfoDetail(DetailView):
    model = UserProfileInfo
    context_object_name = 'userinfo'



class UserProfileInfoUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfileInfo
    fields ='__all__'

    #def get_object(self, *args, **kwargs):
       #pk = self.kwargs['pk']
        #return get_object_or_404(UserProfileInfo, pk=pk)

    #def get_success_url(self):
       # return reverse('accounts:profile')


        
class UsersList(ListView):
    model = UserProfileInfo
    context_object_name = 'users_list'
    queryset = UserProfileInfo.objects.filter(user__groups__name='teachers')
    template_name = 'users.html'

class StudentsList(ListView):
    model = UserProfileInfo
    context_object_name = 'student_list'
    template_name = 'students.html'
    def get_queryset(self):
        return UserProfileInfo.objects.filter(~Q(user__groups__name='teachers'))

class TableStudentsList(ListView):
    model = User
    context_object_name = 'student_list'
    template_name = 'students_table.html'
    def get_queryset(self):
        return User.objects.filter(~Q(groups__name='teachers')).order_by('username').prefetch_related('groups',)

class GroupsStudentsList(ListView):
    model = User
    context_object_name = 'student_list'
    template_name = 'students_groups.html'
    def get_queryset(self):
        return User.objects.filter(~Q(groups__name='teachers')).prefetch_related('groups',)

class LabAllStudentsList(ListView):
    model = User
    template_name = 'lab_all_students.html'
    context_object_name = 'list'
    
    def get_queryset(self, *args, **kwargs):
        student_list = User.objects.filter(~Q(groups__name='teachers')).prefetch_related('groups',)
        course = self.kwargs['course']
        context = [student_list,course]
        print(context)
        return context
    '''
    def get_queryset(self):
        #course = self.kwargs['course']
        return User.objects.filter(~Q(groups__name='teachers')).prefetch_related('groups',)
'''
class TeacherCourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        #print(user)
        return Course.objects.filter(teacher__user__pk=pk)



class AddCourseView(LoginRequiredMixin, generic.CreateView):
    model = Course
    fields = ('name', )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user.userprofileinfo
        base_dir = settings.MEDIA_ROOT
        course_dir = os.path.join(base_dir,'MEDIA_URL','courses')
        
        self.object.url = os.path.join(course_dir, str(form.data.get('name')))
    
        if not os.path.exists(self.object.url):
            os.mkdir(self.object.url)
            self.object.save()
        
        return super().form_valid(form)

class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = Course

    success_url = reverse_lazy('post_list')


class CreateStudyDocView(LoginRequiredMixin, generic.CreateView):
    model = StudyDoc
    fields = ('name', 'document' ,'course')
    success_url = reverse_lazy('users')

    


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user.userprofileinfo
        print("Course - ")
        print(self.object.course)
        return super().form_valid(form)


class CreateStudyDocCommonView(LoginRequiredMixin, generic.CreateView):
    model = StudyDoc
    fields = ('name', 'document')
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user.userprofileinfo
        #self.object.course = ""
        self.object.common = True
        return super().form_valid(form)


class StudyDocCommonView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = StudyDoc
    context_object_name = 'studydoc_list'
    template_name = 'studydoc_list.html'

    def get_queryset(self):
        return StudyDoc.objects.filter(common=True)

class StudyDocList(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = StudyDoc
    context_object_name = 'studydoc_list'
    template_name = 'studydoc_list.html'

    def get_queryset(self, *args, **kwargs):
        user = self.kwargs['user']
        course = self.kwargs['course']
        return StudyDoc.objects.filter(teacher__user__username=user).filter(course__name=course)


class StudyDocDeleteView(LoginRequiredMixin,DeleteView):
    model = StudyDoc

    success_url = reverse_lazy('users')


class StudyDocDetailView(DetailView):
    model = StudyDoc

    def delete(request):
        self.object = self.get_object()


        self.object.delete()
        return HttpResponseRedirect(success_url)


class DiplomaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diploma
    fields = ('theme', 'student')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user.userprofileinfo
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        teacher = self.object.teacher.id 
        return reverse_lazy( 'diploma_list', kwargs={'pk': teacher})


class DiplomaList(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Diploma
    context_object_name = 'diploma_list'
    template_name = 'diploma_list.html'

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        return Diploma.objects.filter(teacher__user__pk=pk)



class LabInfoCreateView(LoginRequiredMixin, generic.CreateView):
    model = LabInfo
    fields = ('course','lab_name', 'lab_number', 'link1', 'link2')

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        return super().form_valid(form)

    def get_success_url(self,*args, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy( 'labs', kwargs={'pk': pk})

class LabInfoListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = LabInfo
    context_object_name = 'lab_list'
    template_name = 'lab_list.html'

    def get_queryset(self, *args, **kwargs):
        course = self.kwargs['pk']
        return LabInfo.objects.filter(course__pk=course)

class LabInfoDetailView(DetailView):
    model = LabInfo


class LabInfoDeleteView(LoginRequiredMixin,DeleteView):
    model = LabInfo

    def get_success_url(self,*args, **kwargs):
        course = self.kwargs['course']
        return reverse_lazy( 'labs', kwargs={'pk': course})


#Lab journal

class LabCreateView(LoginRequiredMixin, generic.CreateView):
    model = Lab
    fields = ('student','lab')

    def get_queryset(self, *args, **kwargs):
        course = self.kwargs['course']
        return reverse_lazy( 'lab_table', kwargs={'course': course})

class LabDetailView(DetailView):
    model = Lab

class LabUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfileInfo
    fields = ('approved')
    template_name = 'lab_approve.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.approve_date = timezone.now()

        return super().form_valid(form)

    
class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ('title', 'text',)
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    tempalte_name = 'blog/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True,author=self.request.user.id).order_by('created_date')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post

    success_url = reverse_lazy('post_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def approve_lab(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    lab.approve()
    course = lab.lab.course
    return redirect('lab_table', course=course)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def register(request):
    

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

  
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.profile_pic = 'MEDIA_URL/profile_pics/default.jpg'

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            print(registered)
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration/registration.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered':registered,
        })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                print('user: {} login'.format(username))
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("LOgIN AND FAIL")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render(request,'basic_app/login.html',{})