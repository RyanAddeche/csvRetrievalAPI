<<<<<<< HEAD
from django.urls import path
from .views import GetRowView

urlpatterns = [
    # Define the URL pattern for the GetRowView
    path('row/', GetRowView.as_view(), name='row'),
=======
from django.urls import path
from .views import GetRowView

urlpatterns = [
    # Define the URL pattern for the GetRowView
    path('row/', GetRowView.as_view(), name='row'),
>>>>>>> 6e1a9bff5ec84b0dd686fff8e270c43ea54a893d
]