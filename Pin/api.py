from app.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'customer', CustomerView, basename='customer')
router.register(r'category', CategoriesView, basename='category')
router.register(r'service', ServicesView, basename='service')
router.register(r'new', NewsView, basename='new')
router.register(r'complaint', ComplaintsView, basename='complaint')
router.register(r'order', OrdersView, basename='order')
router.register(r'order_by_category', OrdersByCategoryView, basename='order_by_category')
router.register(r'payment', PaymentView, basename='payment')