from django.urls import path
from . import views
urlpatterns = [
    path('skills/',views.skills, name="skills"),
    path('res/',views.resume, name="resume"),
]
