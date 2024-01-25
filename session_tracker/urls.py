from django.urls import path

from . import views

app_name = 'session_tracker'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('new_client/', views.new_client, name='new_client'),
    path('subtract_session/<int:client_id>', views.subtract_session, name='subtract_session'),
    path('add_session/<int:client_id>', views.add_session, name='add_session')
]