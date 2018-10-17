from django.urls import path
from . import views



urlpatterns = [
    path('location/',views.Location, name="location"),
    path('analysis/',views.Analysis, name="analysis"),
    path('visualise/',views.Visualise, name="visualise"),
    path('<int:id>/',views.GraphTypeChoosen, name="graph_type"),
    path('',views.homepage, name="home")
]
