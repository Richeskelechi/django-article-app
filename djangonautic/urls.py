from django.contrib import admin
from django.urls import path, include, re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('', article_views.article_list, name="home"),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^assets/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
