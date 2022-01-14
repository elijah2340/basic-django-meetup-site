from django.urls import path
from . import views
from .views import PostCreateView

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>/reg-success/', views.reg_success, name="regsuccess"),
    path('<slug:slug>', views.meetup_details, name="meetup-details"),
    path('create/', PostCreateView.as_view(), name='post-create')
]
