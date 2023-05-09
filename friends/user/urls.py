from django.urls import path

from . import views

urlpatterns = [
    path('register/<str:userName>', views.createUser),
    path('friend/request/<str:userName1>/<str:userName2>', views.createApplication),
    path('friend/accept/<int:application_id>', views.acceptApplication),
    path('friend/refuse/<int:application_id>', views.refuseApplication),
    path('applications/incoming/<int:application_id>', views.refuseApplication),
    path('applications/outgoing/<int:application_id>', views.refuseApplication),
    path('friendList/<str:userName>', views.refuseApplication),
    path('status/<str:userName1>/<str:userName2>', views.refuseApplication),
]