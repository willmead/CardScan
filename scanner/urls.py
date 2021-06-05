from django.urls import path

from . import views

app_name = 'scanner'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.AddCardView.as_view(), name='add'),
    path('scan', views.scan_card, name="scan")
]
