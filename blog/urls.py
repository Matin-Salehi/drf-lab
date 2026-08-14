from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.index, name='index'),
    path('blog/cbv', views.IndexView.as_view(), name='index'),
]