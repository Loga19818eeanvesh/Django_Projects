from dataclasses import field
from multiprocessing import context
from re import template
from typing import List
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

def store_file(file):
    with open("temp/image.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView1(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form" : form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST,request.FILES)
        if submitted_form.is_valid():
            #store_file(request.FILES["user_image"])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return redirect("profiles")

        return render(request, "profiles/create_profile.html",{
            "form" : submitted_form
        })
