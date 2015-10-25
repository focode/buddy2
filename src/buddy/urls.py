from django.conf.urls import include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
from . import buddyactionsview

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^uprofile/', views.UserProfiles.as_view(), name='usersprofile'),
    url(r'^boozProfiles/', views.BoozProfiles.as_view(), name='boozProfiles'),
    url(r'^locateDrinkers/', views.LocateDrinkers.as_view(), name='locateDrinkers'),
    url(r'^GuestList/', views.GuestList.as_view(), name='GuestList'),
    url(r'^YourJoingList/', buddyactionsview.YourJoingList.as_view(), name='YourJoingList'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url( r'^api/', include( 'buddyapi.urls' ) ),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
