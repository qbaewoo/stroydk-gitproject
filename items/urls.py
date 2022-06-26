from django.urls import path
from . import views

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:id>', views.detail, name='detail'),
    path('search', views.search, name='search'),

]