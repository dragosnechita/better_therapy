from django.urls import path
from .views import HomeView
from .views import ClientView, ClientAddView, ClientListView, ClientDetailView, ClientUpdateView, ClientArchiveView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('client/', ClientView.as_view(), name='client'),  # add path with client_ID
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),  # add path with client_ID
    path('client_add/', ClientAddView.as_view(), name='client_add'),
    path('client_list/', ClientListView.as_view(), name='client_list'),  # add path with therapist ID
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'), # add path with client ID
    path('client_archive/<int:pk>', ClientArchiveView.as_view(), name='client_archive'), # add path with client ID

]