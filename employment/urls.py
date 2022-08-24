from django.urls import path
from .views import DetailEmployment, Employments

urlpatterns = [
    path('employment/', Employments.as_view()),
    path('employment/<int:employment_id>/', Employments.as_view()),
    path('employment/detail/<int:employment_id>/', DetailEmployment.as_view()),
]
