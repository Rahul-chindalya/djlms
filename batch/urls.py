from django.urls import path
from batch import views

app_name="batches"

urlpatterns =[
    path('Batchlist/',views.BatchListApi.as_view(),name='Batchlist'),
    path('Batchdetail/<int:pk>',views.BatchDetailsAPI.as_view(),name='Batchdetail'),
]