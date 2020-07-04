from django.urls import path
from contactmanager.page_views.home import HomeView
from contactmanager.page_views.create_profile import CreateProfileView
from contactmanager import views

urlpatterns= [
    path("", HomeView.as_view() , name="home"),
    path("profile", CreateProfileView.as_view(), name="profile")
]

