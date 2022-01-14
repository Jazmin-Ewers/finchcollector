from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'finches/' - Finches Index Route
    path('finches/', views.finches_index, name='finches_index'),

    # 'finches/<int:finch_id>/' - Finches Details Route
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),

    # 'finches/create - Finches Create Route'
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),

    # 'finches/<int:pk>/update - Finches Update Route'
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),

    # 'finches/<int:pk>/delete - Finches Delete Route'
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),

]