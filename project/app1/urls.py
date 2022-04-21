from django.urls import path, include
from .views import ContributorListView, PageView, PageView2, PageView3
from django.views.generic import ListView

urlpatterns = [
    path('/contributors/', ContributorListView.as_view()),
    path('/main/', PageView.as_view()),
    path('/information/', PageView2.as_view()),
    path('/help_us/', PageView3.as_view())
]
