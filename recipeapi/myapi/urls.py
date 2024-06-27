from django.urls import path
from .views import RecipeListCreate, RecipeRetrieveUpdateDestroy

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-view-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroy.as_view(), name='recipe-view-update-delete'),
]
