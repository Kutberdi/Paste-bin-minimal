from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_paste, name='create_paste'),
    path('paste/<int:paste_id>/', views.view_paste, name='view_paste'),
    path('paste/<int:paste_id>/delete/', views.delete_paste, name='delete_paste'),
]