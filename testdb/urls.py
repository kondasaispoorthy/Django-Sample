from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.StudentList,name='student-list'),
    path('get/<str:pk>/',views.StudentDetail,name='student-detail'),
    path('create/',views.StudentCreate,name='student-create'),
    path('update/<str:pk>/',views.StudentUpdate,name='student-update'),
    path('delete/<str:pk>/',views.StudentDelete,name='student-delete'),

]