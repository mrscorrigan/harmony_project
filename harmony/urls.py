"""harmony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from harmony_app.views import get_index
from harmony_app import views
from accounts import views as accounts_views
from harmony_app import views as harmony_views
from settings import MEDIA_ROOT
from django.views.static import serve
from accounts.views import cancel_subscription

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', harmony_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'', include ('blog_app.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
    url(r'^cancel/$', accounts_views.cancel, name='cancel'),



]

