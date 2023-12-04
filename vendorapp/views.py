from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from datetime import datetime, timedelta
from datetime import timezone, datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


# Create your views here.

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class VendorListAPIView(APIView):
    def get(self, request):
        vendor_obj = Vendor.objects.all()
        serializer = VendorSerializer(vendor_obj, many=True)
        data = serializer.data
        return Response({'status': 200, 'payload': data})

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class VendorDetailAPIView(APIView):
    def get(self, request, pk):
        vendor_obj = get_object_or_404(Vendor, pk=pk)
        serializer = VendorSerializer(vendor_obj, context={'request': request})
        return Response({'status': 200, 'Payload': serializer.data})

    def put(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)
        serializer = VendorSerializer(vendor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})

    def delete(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)
        vendor.delete()
        return Response({'status': 204, 'Payload': 'Vendor deleted'})
    
@action(detail=True, methods=['GET'], url_path='performance')
def get_performance_metrics(self, request, pk=None):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_data)






    



#PURCHASE ORDER VIEWSET

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_create(self, serializer):
        serializer.save()
        # Calculate and update on-time delivery rate for the vendor
        vendor = serializer.validated_data['vendor']
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
        on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        old_status = self.get_object().status
        serializer.save()
        new_status = serializer.validated_data.get('status', old_status)
        vendor = serializer.validated_data['vendor']
        if old_status != new_status or new_status == 'completed':
            vendor.update_performance_metrics()



    @action(detail=True, methods=['POST'], url_path='acknowledge')
    def acknowledge_purchase_order(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Recalculate average_response_time for the vendor
        vendor = purchase_order.vendor
        response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False) \
            .exclude(acknowledgment_date__gt=timezone.now()) \
            .aggregate(avg_response_time=models.Avg(models.F('acknowledgment_date') - models.F('issue_date')))
        vendor.average_response_time = response_times['avg_response_time'].total_seconds() / 3600  # convert to hours
        vendor.save()

        return Response({'status': 'Acknowledged'})



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        historical_data = HistoricalPerformance.objects.filter(vendor_id=vendor_id)
        serializer = HistoricalPerformanceSerializer(historical_data, many=True)
        return Response({'status': 200, 'payload': serializer.data})


