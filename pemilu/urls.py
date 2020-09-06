from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('hello', views.hello, name='hello'),
    path('login', views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path("result", views.result, name="result"),
    path("home", views.home, name="home"),
    path("save", views.save, name="save"),
    path("prospect", views.prospect, name="prospect"),
    path("gaji", views.gaji, name="gaji"),
    path("portofolio", views.portofolio, name="portofolio"),
    path("everyday", views.everyday, name="everyday"),
    path("every", views.every, name="every"),
    path("dream", views.dream, name="dream"),
    path("deposit", views.deposit, name="deposit"),
    path("read", views.read, name="read"),
    path("future", views.future, name="future"),
    path("literacy", views.literacy, name="literacy")
]
