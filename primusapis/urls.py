from django.urls import path
from django.contrib import admin



from .views import *
urlpatterns = [
    path('statusnotification/', MarkedAsSafeNotification.as_view()),
    path('status/', Marked_as_safe.as_view()),
    path('location/', Location.as_view()),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),

]
