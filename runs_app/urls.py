from django.urls import path
from . import views


# register the app namespace
# URL NAMES
app_name = 'runs_app'

urlpatterns = [
    path('', views.runs_view, name='runs_view'),
    path('run/', views.run_view, name='run_view'),
]
