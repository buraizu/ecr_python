from django.urls import path
from . import views


# register the app namespace
# URL NAMES
app_name = 'runs_app'

urlpatterns = [
    path('', views.list_runs, name='list_runs'),
    path('run/', views.run_detail, name='run_detail'),
]
