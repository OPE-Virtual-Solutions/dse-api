from django.urls import path

from .views import *

urlpatterns = [
    path('bairros/', TbBairroAPIView.as_view(), name='bairros'),
]
