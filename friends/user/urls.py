from django.urls import path

from . import views

urlpatterns = [
    path('register/<str:userName>', views.createUser),
    path('applications/create/<str:userName1>/<str:userName2>', views.createApplication),
    path('applications/accept/<int:application_id>', views.acceptApplication),
    path('applications/refuse/<int:application_id>', views.refuseApplication),
    path('applications/incoming/<str:userName>', views.incomingApplication),
    path('applications/outgoing/<str:userName>', views.outgoingApplication),
    path('friendList/<str:userName>', views.friendList),
    path('status/<str:userName1>/<str:userName2>', views.status),
    path('delete/<str:userName1>/<str:userName2>', views.deleteFriend),
]