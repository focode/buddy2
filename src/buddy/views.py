from django.views import generic
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from . import forms
from django.template.response import TemplateResponse
from buddyutility import getAddress
from django.shortcuts import render_to_response
from models import usersProfiles
from models import boozProfiles
from models import locateDrinkers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
          #
          form.save()

          # Render the success page.
          return render(request, "addprofile.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.UserProfileForm(request.POST)
            return render(request, "addprofile.html", { 'form' : form })

    def post(self, request, *args, **kwargs):
        template_name = "addprofile.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = usersProfiles
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          #
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
        form = forms.boozProfilesForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          print request.POST
          form.save()

          # Render the success page.
          return render(request, "boozinvite.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.boozProfilesForm(request.POST)
            return render(request, "boozinvite.html", { 'form' : form })

    def post(self, request, *args, **kwargs):
        template_name = "boozinvite.html"
        http_method_names = ['get', 'post']
        userTemp = self.request.user
        models = boozProfiles
        form = forms.boozProfilesForm(request.POST)

        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          print form.cleaned_data['datetime']
          print form.cleaned_data
          latitude = form.cleaned_data['Booz_shop_location'][0]
          longitude = form.cleaned_data['Booz_shop_location'][1]
          print latitude,longitude

          address = getAddress(latitude,longitude)
          print "User name is ::", userTemp

          tempAddress = form.save(commit=False)
          tempAddress.boozshopaddress = address
          tempAddress.user = userTemp
          tempAddress.save()


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

    def post(self, request, *args, **kwargs):
        template_name = "drinkersList.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        form = forms.LocateDrinkersForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          searchAttributes = form.save(commit=False)
          print "searchAttributes.boozshopaddress", searchAttributes.boozshopaddress
          #searchResults = boozProfiles.objects.filter(Booz_shop_location__icontains=searchAttributes.boozshopaddress)
          searchResults = boozProfiles.objects.all()
          paginator = Paginator(searchResults, 25) # Show 25 contacts per page
          page = request.GET.get('page')
          print "searchResults.query", searchResults.query
          print "searchResults::" ,str(searchResults)
          try:
              profilePerPages = paginator.page(page)
          except PageNotAnInteger:
              profilePerPages = paginator.page(1)
          except EmptyPage:
              profilePerPages = paginator.page(paginator.num_pages)

          return render_to_response("drinkersList.html", {"profilePerPages": profilePerPages})


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


class GuestList(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "guestList.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        response = TemplateResponse(request, 'guestList.html', {})
        return response




