from django.urls import path
from . import views

app_name = 'maangas'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:maanga_id>/', views.detail, name = 'detail'),
    path('<int:maanga_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
    path('<int:maanga_id>/<int:chapter_id>', views.chapter, name = 'chapter'),
]

