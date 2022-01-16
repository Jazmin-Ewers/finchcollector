from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'tables/' - Finches and Toys Route'
    path('tables/', views.finches_toys_index, name='finches_toys_index'),

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

    # 'finches/<int:finch_id>/add_feeding - Add Finch's feeding Route'
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    # 'finches/<int:finch_id>/assoc_toy/<int:toy_id>/- Add Finch's toy'
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

    # 'finches/<int:cat_id>/unassoc_toy/<int:toy_id>/'- Add toys not associated with Finch'
    path('finches/<int:finch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),

    # 'toys/' - Toys Index Route
    path('toys/', views.ToyList.as_view(), name='toys_index'),

    # 'toys/<int:pk>/' - Toys Details Route
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),

    # 'toys/create/' - Toys Create Route'
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),

    # 'toys/<int:pk>/update/' - Toy Update Route'
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    
    # 'toys/<int:pk>/delete/' - Toy Delete Route'
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

]