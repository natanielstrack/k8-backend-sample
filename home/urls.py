from django.urls import path

from home import views


urlpatterns = [
    path('version', views.ViewVersion.as_view(), name='version')
]
