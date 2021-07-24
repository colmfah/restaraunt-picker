from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_restaraunts, name='restaraunts'),
    path('<restaraunt_id>', views.restaraunt_detail, name='restaraunt_detail'),
]