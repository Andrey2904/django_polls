from django.urls import path
from .views import index, rubric_bbs

urlpatterns = [
    path('<int:rubric_id>/', rubric_bbs, name = 'rubric_bbs' ),
    path('', index, name = 'index'),  # Пример маршрута
]