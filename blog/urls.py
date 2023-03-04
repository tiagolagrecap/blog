

from django.urls import path
from .views import index, post_delete, post_update, post_view


urlpatterns = [
    path('', index, name='index'),
    path('post_delete/<int:pk>/', post_delete, name='post-delete'),
    path('post_update/<int:pk>/', post_update, name='post-update'),
    path('post_view/<int:pk>/', post_view, name='post-view'),

]
