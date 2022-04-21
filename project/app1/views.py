from django.shortcuts import render
from django.views.generic import ListView
from .models import Contributor


class PageView(ListView):
    template_name = 'main.html'
    queryset = ''


class PageView2(ListView):
    template_name = 'information.html'
    queryset = ''


class PageView3(ListView):
    template_name = 'help_us.html'
    queryset = ''


class ContributorListView(ListView):
    model = Contributor
    template_name = 'contributor.html'
    context_object_name = 'contributor'
    queryset = Contributor.objects.all()
    queryset = queryset.order_by('-donated_amount')

