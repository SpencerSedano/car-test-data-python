from django.urls import path

from . import views


app_name = "quiz"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_number>/", views.detail, name="detail"),
]
