from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'finches/' - Finches Index Route
    path('finches/', views.finches_index, name='finches_index'),

    # 'finches/<int:finch_id>/' - Finches Details Route
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail')

]