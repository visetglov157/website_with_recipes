from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/user', views.recipe_user, name='recipe_user'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/add/', views.recipe_add, name='recipe_add'),
    path('recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]