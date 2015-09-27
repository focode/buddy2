from django.views import generic
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from . import forms

from models import usersProfiles
from models import boozProfiles
from models import locateDrinkers


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class UserProfiles(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = "addprofile.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = usersProfiles
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          form.save()

          # Render the success page.
          return render(request, "addprofile.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.UserProfileForm(request.POST)
            return render(request, "addprofile.html", { 'form' : form })

class BoozProfiles(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = "boozinvite.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = boozProfiles
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          form.save()

          # Render the success page.
          return render(request, "boozinvite.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.boozProfilesForm(request.POST)
            return render(request, "boozinvite.html", { 'form' : form })

class LocateDrinkers(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = "locatedrinkers.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        form = forms.LocateDrinkersForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          form.save()

          # Render the success page.
          return render(request, "locatedrinkers.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.LocateDrinkersForm(request.POST)
            return render(request, "locatedrinkers.html", { 'form' : form })

class GuestEntry(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = "locatedrinkers.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        form = forms.LocateDrinkersForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          form.save()

          # Render the success page.
          return render(request, "locatedrinkers.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.LocateDrinkersForm(request.POST)
            return render(request, "locatedrinkers.html", { 'form' : form })



