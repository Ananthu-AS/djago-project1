from django.urls import path
from hr import views
urlpatterns = [
    path('',views.index,name="hr"),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
]