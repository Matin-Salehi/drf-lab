from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.index, name='index'),
    path('blog/cbv', views.IndexView.as_view(), name='index'),
    path('crypto', views.GetCryptoPrice.as_view(), name='crypto'),
    path('ser', views.SerializerView.as_view(), name='ser'),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('articles/add', views.AddArticleView.as_view(), name='add'),
]