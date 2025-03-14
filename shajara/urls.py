from django.urls import path
from .views import person_list_create, person_detail

urlpatterns = [
    
    # CRUD endpoints
    path('persons/', person_list_create, name='person-list-create'),
    path('persons/<int:pk>/', person_detail, name='person-detail'),
]
