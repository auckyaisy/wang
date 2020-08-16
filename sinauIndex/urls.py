from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),
    path('profile', views.profile, name='profile'),
    path('timetable', views.timetable, name='timetable'),
    path('meet', views.meet, name='meet'),
    path('notes', views.notes, name='notes'),
    path('qna', views.qna, name='qna'),
    path('qna/1', views.qna1, name='qna1'),
    path('search', views.search, name='search'),
    path('assignment', views.assignment, name='assignment'),
    path('assignment/1', views.assign1, name='assign1'),
    path('courses', views.courses, name='courses'),
    path('coursesplayer/', views.coursesplayer, name='coursesplayer'),
    path('coursesplayer/1', views.coursesplayer1, name='coursesplayer1'),
    # path('login', views.login_view, name='login'),
    # path("logout", views.logout_view, name="logout")
]
