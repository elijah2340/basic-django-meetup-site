from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm
from django.views.generic import CreateView


# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'mymeetups/index.html', {
        'meetups': meetups
    })


class PostCreateView(CreateView):
    model = Meetup
    fields = ['title', 'slug', 'description', 'image', 'organiser', 'date', 'location']
    template_name = 'mymeetups/postform.html'

    def form_valid(self, form):
        return super(PostCreateView, self).form_valid(form)


def meetup_details(request, slug):
    selected_meetup = Meetup.objects.get(slug=slug)
    if request.method == 'GET':
        registration_form = RegistrationForm()
    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data['email']
            participant, was_created = Participant.objects.get_or_create(email=user_email)
            return redirect('regsuccess', slug=slug)
    return render(request, 'mymeetups/meetup-details.html', {
        'meetup':  selected_meetup,
        'form': registration_form,
    }, )


def reg_success(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, 'mymeetups/reg-success.html',{
        'organiser': meetup.organiser,
    })



