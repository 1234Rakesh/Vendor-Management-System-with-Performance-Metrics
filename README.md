# Vendor-Management-System

# Vendor Management System API

## Overview

This Django-based Vendor Management System API allows you to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Adi7936/Vendor-Management-System.git
   cd vendor-management-api

2.Install Dependencies:
pip install -r requirements.txt
3.Apply Migrations:
python manage.py migrate and python manage.py makemigrations
4.Create Superuser:
python manage.py createsuperuser
5.Run Development Server:
python manage.py runserver
Access Admin Panel:

Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Obtain Token:

Create a token for the superuser in the Django admin panel (/admin/authtoken/token/). Use this token for API authentication.

API Endpoints
Vendor Management
List/Create Vendors:

Endpoint: /api/vendors/
Method: GET (List all vendors) / POST (Create a new vendor)
Retrieve/Update/Delete Vendor:

Endpoint: /api/vendors/{vendor_id}/
Method: GET (Retrieve) / PUT (Update) / DELETE (Delete)
Vendor Performance Metrics:

Endpoint: /api/vendors/{vendor_id}/performance/
Method: GET
Purchase Order Tracking
List/Create Purchase Orders:

Endpoint: /api/purchase_orders/
Method: GET (List all purchase orders) / POST (Create a new purchase order)
Retrieve/Update/Delete Purchase Order:

Endpoint: /api/purchase_orders/{po_id}/
Method: GET (Retrieve) / PUT (Update) / DELETE (Delete)
Acknowledge Purchase Order:

Endpoint: /api/purchase_orders/{po_id}/acknowledge/
Method: POST


Token Authentication
To access secured endpoints, include the token in the Authorization header:
Authorization: Token your-token-here

Test Suite
A comprehensive test suite is available in the tests directory. Run tests using:
python manage.py test


This README file provides basic setup instructions, details on API endpoints, and mentions a test suite. Adjust the content based on your project's specific details and requirements.

NOTE:HERE I DID'NT MENTIONED ALL API ENDPOINTS PLEASE CHECK INSIDE MY CODE YOU WILL CORRECT AND ALL API END POINTS
