from django.urls import path
from .views import PubListView, PubDetailView


urlpatterns = [
    path('', PubListView.as_view(), name="pub"),
    path('<int:pk>', PubDetailView.as_view(), name="publisher_detail"),
]
