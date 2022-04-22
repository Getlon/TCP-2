from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Contributor
from .forms import EventForm
from .models import Event
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


class PageView(ListView):
    template_name = 'main.html'
    queryset = ''


class PageView2(ListView):
    template_name = 'information.html'
    queryset = ''


class PageView3(ListView):
    template_name = 'help_us.html'
    queryset = ''


class PageView4(ListView):
    template_name = 'inter_places.html'
    queryset = ''


class ContributorListView(ListView):
    model = Contributor
    template_name = 'contributor.html'
    context_object_name = 'contributor'
    queryset = Contributor.objects.all()
    queryset = queryset.order_by('-donated_amount')


class Events(ListView):
    model = Event
    template_name = 'add_event.html'
    context_object_name = 'events'
    queryset = Event.objects.all()
    form_class = EventForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class EventsListView(ListView):
    model = Event
    template_name = 'events_view.html'
    context_object_name = 'item'
    queryset = Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'item'
    queryset = Event.objects.all()
