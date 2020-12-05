from django.urls import path
from . import views
from .views import (
    DetailListView,
    DetailDetailView,
    DetailCreateView,
    DetailUpdateView,
    DetailDeleteView,
    UserDetailListView
)


urlpatterns = [
    path('', DetailListView.as_view(), name='match_home'),
    path('user/<str:username>', UserDetailListView.as_view(), name='user_detail'),
    path('detail/<int:pk>/', DetailDetailView.as_view(), name='detail_detail'),
    path('detail/new/', DetailCreateView.as_view(), name='detail_create'),
    path('detail/<int:pk>/update/', DetailUpdateView.as_view(), name='detail_update'),
    path('detail/<int:pk>/delete/', DetailDeleteView.as_view(), name='detail_delete'),
    path('about/', views.about, name='match_about')

]



