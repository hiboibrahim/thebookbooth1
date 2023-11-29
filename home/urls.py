from django.urls import path
# from . import views
from .views import BookList

urlpatterns = [
    path('', BookList.as_view(), name='home')
]