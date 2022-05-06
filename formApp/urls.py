from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.base,name='base'),
    path('/update/<int:stdId>',views.update,name='update'),
    path('deleted/<int:stdId>/',views.delete,name='delete'),
    path('api/',include('formApp.api.urls'))
]
