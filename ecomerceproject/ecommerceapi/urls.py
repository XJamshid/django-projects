from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import (
    UrlsAPIView,
    CategoryListAPIView,
    AccountDetailAPIView,
    HomeListAPIView,
    CartDetailAPIView,
    CategoryProductListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    CartItemCreateAPIView,
    CartCreateAPIView,
    CartItemQuantityUpdateAPIView,
    ShippingAddressCreateAPIView,
    ShipmentAPIView,
    ShipmentListAPIView,
    RegistrationAPIVIew,
    CommentCreateAPIView,
    LikeAPIView,
    CustomerShipmentListAPIView,
    WishListAPIView,
    RecommendationsListAPIView,
    LowPricesListAPIView,
    NewAdditionsListAPIView,
    OrderItemDeleteView,
    ProfileUpdateAPIView,
    ShippingAddressListAPIView,
    ShippingAddressUpdateAPIView,
    #ProductCreateAPIView,
    #ProductImageCreateAPIView,
    #CategoryCreateAPIView,
    #CustomAuthToken
    #LoginAPIView
)

urlpatterns=[
    path('',UrlsAPIView.as_view(),name='navbar'),
    path('home/', HomeListAPIView.as_view(), name='home'),
    path('home/recommendations/', RecommendationsListAPIView.as_view(), name='recommendations'),
    path('home/low_prices', LowPricesListAPIView.as_view(), name='low_prices'),
    path('home/new_additions', NewAdditionsListAPIView.as_view(), name='new_additions'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    #path('categories/add/', CategoryCreateAPIView.as_view(), name='category_add'),
    path('categories/<slug:slug>/', CategoryProductListAPIView.as_view(), name='category'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    #path('products/add', ProductCreateAPIView.as_view(), name='products_add'),
    #path('product_image/add', ProductImageCreateAPIView.as_view(), name='product_image_add'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product'),
    path('products/<slug:slug>/comment', CommentCreateAPIView.as_view(), name='comment_create'),
    path('products/<slug:slug>/like', LikeAPIView.as_view(), name='like'),
    path('cart/', CartDetailAPIView.as_view(), name='cart'),
    path('account/', AccountDetailAPIView.as_view(), name='account'),
    path('account/shipments/', CustomerShipmentListAPIView.as_view(), name='customer_shipments'),
    path('account/wishlist/', WishListAPIView.as_view(), name='wishlist'),
    path('account/edit_profile/<int:pk>/', ProfileUpdateAPIView.as_view(), name='profile_edit'),
    path('add_to_cart/<slug:slug>/', CartItemCreateAPIView.as_view(), name='add_to_cart'),
    path('cart_create/', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart/update_quantity/<int:pk>/', CartItemQuantityUpdateAPIView.as_view(), name='update_quantity'),
    path('cart/product_remove/<int:pk>/', OrderItemDeleteView.as_view(), name='product_remove'),
    path('shipping_address_create/', ShippingAddressCreateAPIView.as_view(), name='shipping_address_create'),
    path('shipping_address/', ShippingAddressListAPIView.as_view(), name='shipping_address'),
    path('shipping_address/<int:pk>/edit/', ShippingAddressUpdateAPIView.as_view(), name='shipping_address_edit'),
    path('shipment/', ShipmentAPIView.as_view(), name='shipment'),
    path('shipments/', ShipmentListAPIView.as_view(), name='shipment_list'),
    path('registration/', RegistrationAPIVIew.as_view(), name='registration'),
    #path('login/', ObtainAuthToken.as_view(), name='login'),
    #path('login/', LoginAPIView.as_view(), name='login'),
]