from django.urls import path

from . import views

app_name = 'librarydb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateBookView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete'),
    path('<int:pk>/', views.UpdateBookView.as_view(), name='update'),
]