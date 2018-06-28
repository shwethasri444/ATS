from django.urls import path,re_path

from cupid import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('icons/', views.icons, name='icons'),
    path('contact/', views.contact, name='contact'),
    path('jobs/', views.jobs, name='jobs'),
    path('login/', views.pagelogin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('professional/', views.professional, name='professional'),
    path('register/', views.register, name='register'),
    path('single/', views.single, name='single'),
    path('codes/', views.codes, name='codes'),
    path('upload/', views.upload, name='upload'),
    path('location_single/', views.location_single, name='location_single'),
    # path('results/', views.display_result, name='results'),
    re_path('results/(\d+)/',views.display_result, name='results'),
    path('user_profile/', views.jdtable, name='user_profile'),
    path('jd/', views.addjd, name='addjd'),
    re_path(r'^candidate_profile/(?P<username>[a-zA-Z0-9]+)/$',views.candidate_profile_page, name='candidate_profile'),
    re_path(r'^recruiter_profile/(?P<username>[a-zA-Z0-9]+)/$',views.recruiter_profile_page, name='recruiter_profile'),
]