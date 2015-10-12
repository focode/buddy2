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




class GuestList(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "guestList.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        response = TemplateResponse(request, 'guestList.html', {})
        return response

class YourJoingList(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "yourjoininglist.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        queryvalue = request.GET.get('q', '')
        print queryvalue
        # perform db action here and create joing list and render it here

        response = TemplateResponse(request, 'yourjoininglist.html', {})
        return response

    def post(self, request, *args, **kwargs):
        template_name = "yourjoininglist.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        response = TemplateResponse(request, 'yourjoininglist.html', {})
        return response




