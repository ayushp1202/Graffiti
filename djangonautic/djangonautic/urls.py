from django.urls import include, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.url')),
    re_path(r'^articles/', include('articles.url')),
    re_path(r'^about/$',views.about),
    re_path(r'^$', article_views.article_list,name="home"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)