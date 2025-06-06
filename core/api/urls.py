from django.urls import path
from .views import GetRowView

urlpatterns = [
    # Define the URL pattern for the GetRowView
    path('row/', GetRowView.as_view(), name='row'),
]