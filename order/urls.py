from django.urls import path
from . import views

urlpatterns = [
    path('orders/create/<int:pk>',views.CreateOrderView.as_view(), name='order_create'),
    path('orders/',views.OrderListView.as_view(), name='order'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('cart/add/<int:product>/<int:quantity>',views.AddtoCartView.as_view(), name='add_to_cart'),
]
