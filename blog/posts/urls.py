from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about_view, name='about'),
    path('post/<str:pk>',views.post,name='post')
]
