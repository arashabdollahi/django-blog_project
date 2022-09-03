from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListViews.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
