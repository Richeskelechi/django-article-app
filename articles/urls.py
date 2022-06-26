from django.urls import path
from .import views
app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('create', views.create_article, name="create_article"),
    path('<param>', views.each_list, name="each_list"),
]
