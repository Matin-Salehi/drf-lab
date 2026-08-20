from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    path('blog', views.index, name='index'),
    path('blog/cbv', views.IndexView.as_view(), name='index'),
    path('crypto', views.GetCryptoPrice.as_view(), name='crypto'),
    path('ser', views.SerializerView.as_view(), name='ser'),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('articles/add', views.AddArticleView.as_view(), name='add'),
    path('articles/update/<int:pk>', views.UpdateArticleView.as_view(), name='update'),
    path('token', views.ChackToken.as_view(), name='check_token'),
    path('login', token_views.obtain_auth_token),
]