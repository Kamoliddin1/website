from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)', views.detail_view, name='postw'),
    url(r'^(?P<pk>\d+)', views.Detail.as_view(), name='post'),
    url(r'^$', views.IndexView.as_view(), name='posts'),
]




