from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # should be in a separated app ex. accounts app
    path("login", obtain_auth_token),
    path("signup", views.api_signup),


    path("", views.index),
    path("create", views.create),
    path("edit/<int:id>", views.create),
    path("<int:pk>", views.RudPost.as_view()),
]