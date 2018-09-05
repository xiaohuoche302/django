"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('study01.url')),
    url(r'',include('study02.url')),
    url(r'',include('study03.url')),
    url(r'',include('study04.url')),
    url(r'',include('study05.url')),
    url(r'',include('study06.url')),
    url(r'',include('study07.url')),
    url(r'',include('study08.url')),
    url(r'', include('testwork.url')),
    url(r'',include('calc.url')),
    url(r'axf/', include('mywork01.url',namespace='axf')),
]
