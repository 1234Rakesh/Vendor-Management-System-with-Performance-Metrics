from django.contrib import admin
from django.urls import path,include
from vendorapp import views

urlpatterns = [
    #create vendor
    path('vendor-create/', views.VendorListAPIView.as_view(), name='vendor-list-create'),
    #list of all vendors
    path('vendors/<int:pk>/performance',views.VendorDetailAPIView.as_view(),name='vendor-performance'),
    path('vendors/', views.VendorListAPIView.as_view(), name='get-vendor-list'),
    #get vendor list by id 
    path('vendor/<int:pk>/', views.VendorDetailAPIView.as_view(), name='vendor-detail'),
    #Update/Put Vendors List/Details
    path('vendor/update/<int:pk>', views.VendorDetailAPIView.as_view(), name='vendor-update'),
     #delete vendor 
    path('vendor-delete/delete/<int:pk>/', views.VendorDetailAPIView.as_view(), name='vendor-delete'),

     # Purchase Order URLs

    #CREATE/POST PURCHASE ORDER
    path('create-purchase-order/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
   #List all Purchase Orders with an option to filter by vendor:
    path('get-purchase-orders/', views.PurchaseOrderListCreateView.as_view(), name='get-purchase-order-lists'),
    #Retrieve details of a specific Purchase Order
    path('purchase_order/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('purchase_orders/<int:pk>/acknowledge/', views.PurchaseOrderDetailView.as_view(),name='acknowledge-purchase-order'),
    #Update a Purchase Order:
    path('purchase_order/update/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchase-order-update'),
    #Delete a Purchase Order:
    path('purchase_order/delete/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchase-order-delete'),

    #retrieves a vendor's performance metrics. 
    path('vendors/<int:vendor_id>/performance/', views.VendorPerformanceAPIView.as_view(), name='vendor-performance'),

]
