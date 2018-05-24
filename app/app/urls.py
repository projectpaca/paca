"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView
<<<<<<< HEAD
from django.conf.urls.static import static

from django.contrib.auth.models import Group

admin.site.unregister(Group)
=======
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
>>>>>>> lisa

admin.site.site_header = "PACA Adminportal"
admin.site.site_title = "PACA Adminportal"
admin.site.index_title = "Portalen där administratörer och chefer kan skapa nya, redigera och ta bort användare, arbetspass m.m."

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('fullcalendar/', include('fullcalendar.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls')),
<<<<<<< HEAD
    url('avatar/', include('avatar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += [
#         url('media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT})
#     ]
=======
    # path('accounts/', include('django.contrib.auth.urls')),
]



# path('account/', include('django.contrib.auth.urls', 'accounts.urls')),
# All urls defined in /accounts/urls.py come after the url 'account/'.
>>>>>>> lisa
