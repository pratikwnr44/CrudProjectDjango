from django.urls import path
from .views import OrderView,ShowOrder,updateOrder,deleteOrder, index

urlpatterns = [
    path('ov/', OrderView, name='order_url'),
    path('sv/', ShowOrder, name='show_url'),
    path('uv/<int:pk>/', updateOrder, name='update_url'),
    path('dv/<int:pk>/', deleteOrder, name='delete_url'),
    path('index/', index , name='index_url' )
]