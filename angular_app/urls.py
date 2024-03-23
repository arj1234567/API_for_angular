from django.urls import path
from .views import Userview


urlpatterns = [
    path('user/',Userview.as_view()),
    path('user/<int:id>',Userview.as_view(),)
]
