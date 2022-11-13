"""ecr_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import RedirectView
import runs_app, events_app, runner_events_app


urlpatterns = [
    path('runs_app/', include('runs_app.urls')),
    path('events_app/', include('events_app.urls')),
    path('runner_events_app/', include('runner_events_app.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='events_app/list_events')), # Todo - fix
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', events_app.views.SignUpView.as_view(), name='signup')
]
