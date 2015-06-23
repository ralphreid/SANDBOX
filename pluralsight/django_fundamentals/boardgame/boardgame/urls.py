"""boardgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()  # Tells admin site to discover all models to generate a UI for


# Deprecated since version 1.8: urlpatterns should be a plain list of django.conf.urls.url() instances instead.
# since no '$' it can be several urls under admin which are include by the site.url module
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='boardgames_home')  # when a user logs out they are returned to the page called 'boardgames_home
)


urlpatterns += patterns(
    'django.contrib.auth.views',  # this prefix means that this is the common prefix for the pattern invocation

    url(r'^login/$', 'login',  # so based on the prefix above, its actually looking for 'django.contrib.auth.views.login'
        {'template_name': 'login.html'},
        name='boardgames_login'),  # naming of url mappings

    url(r'^logout/$', 'logout',
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)
