from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.detail, name='detail'),
    path('tripper/<tripper>', views.tripper, name='tripper'),
    path('trips/', views.trips, name='trips'),
    path('trips/<int:id>', views.tripindex, name='tripindex'),
]


