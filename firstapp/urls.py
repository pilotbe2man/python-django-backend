from django.urls import path
from django.conf.urls import url
from .views import ListFirstappsView, FirstappDetail, FirstappCreate


urlpatterns = [
    path('all/', ListFirstappsView.as_view(), name="firstapp-all"),
    url(r'create/', FirstappCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/firstapp/$', FirstappDetail.as_view())
]