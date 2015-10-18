from django.views import generic
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from . import forms
import datetime
from django.template.response import TemplateResponse
from buddyutility import getAddress
from django.shortcuts import render_to_response
from models import usersProfiles
from models import boozProfiles
from models import locateDrinkers
from models import GuestEntry
from guestOperations import saveGuestEntry,getAllJoingList
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
        print "Arunesh::",queryvalue
        boozIdProfileRequest = queryvalue
        joingTime = datetime.datetime.now()
        user_id = user.id

        if queryvalue:
            saveGuestEntry(boozprofileId=boozIdProfileRequest,userId=user_id,likeStatus='True',joiningtime = joingTime)
        #g = GuestEntry(boozprofileId=boozIdProfileRequest,userId=user_id,likeStatus='True',joiningtime = joingTime)
        #g.save()

        # now show all the joining list of the logged in user

        allJoingLists = getAllJoingList()

        # perform db action here and create joing list and render it here
        return render_to_response("yourjoininglist.html", {"allJoingLists": allJoingLists})


    def post(self, request, *args, **kwargs):
        template_name = "yourjoininglist.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = locateDrinkers
        response = TemplateResponse(request, 'yourjoininglist.html', {})
        return response


''' this classs is just of testing purpose '''
'''
class GuestEntry(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "GuestEntry.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = GuestEntry
        form = forms.GuestEntryForm
        # perform db action here and create joing list and render it here
        form = forms.GuestEntryForm(request.POST)
        return render(request, "GuestEntry.html", { 'form' : form })

        '''









