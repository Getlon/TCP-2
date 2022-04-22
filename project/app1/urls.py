from django.urls import path, include
from .views import ContributorListView, PageView, PageView2, PageView3, Events, EventsListView, EventDetailView, PageView4
from django.views.generic import ListView

urlpatterns = [
    path('/contributors/', ContributorListView.as_view()),
    path('/main/', PageView.as_view()),
    path('/information/', PageView2.as_view()),
    path('/help_us/', PageView3.as_view()),
    path('/add_post/', Events.as_view()),
    path('/events_view/', EventsListView.as_view()),
    path('/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('/inter_places/', PageView4.as_view())
]
