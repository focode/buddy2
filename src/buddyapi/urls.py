from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from .views import TaskList, TaskDetail,DummyResponse

urlpatterns = patterns('',

    # Regular URLs
	# url(r'^tasks/$', task_list, name='task_list'),
    # url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),

    # Class based URLs,
    url( r'^tasks/$', TaskList.as_view(), name = 'task_list' ),
    url( r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name = 'task_detail' ),
    url( r'^DummyResponse/(?P<pk>[0-9]+)$', DummyResponse.as_view(), name = 'DummyResponse' ),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])