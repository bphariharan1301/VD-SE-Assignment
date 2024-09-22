from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .models import Order
from .rate_limiter import RateLimiter
import json

# Initialize the rate limiter
rate_limiter = RateLimiter()


# View to get top customers (with token authentication and rate limiter)
@csrf_exempt
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def top_customers_view(request):
    user_id = request.user.id  # Get user ID from the authenticated user

    if not rate_limiter.allow_request(user_id):
        return JsonResponse(
            {"error": "Rate limit exceeded. Try again later."}, status=429
        )

    # Fetch top customers from the database
    top_customers = Order.get_top_customers()

    # Prepare the response data
    response_data = [
        {"customer_id": customer["customer"], "total_spent": customer["total_spent"]}
        for customer in top_customers
    ]

    return JsonResponse(response_data, safe=False)


# View to create users (CSRF exempt)
@csrf_exempt  # Disable CSRF for this view (you can use this in development only)
def create_users_view(request):
    if request.method == "POST":
        try:
            # Load JSON data from the request body
            user_data = json.loads(request.body)
            created_users = []

            # Create users from the provided data
            for user_info in user_data:
                user = User.objects.create_user(
                    username=user_info["username"],
                    password=user_info["password"],
                    email=user_info.get("email", ""),
                    first_name=user_info.get("first_name", ""),
                    last_name=user_info.get("last_name", ""),
                )
                created_users.append(
                    {"id": user.id, "username": user.username, "email": user.email}
                )

            return JsonResponse(created_users, safe=False, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_auth_view(request):
    # Log the headers to see if the token is being received
    print(request.headers)  # This will print the headers in the server logs

    return JsonResponse(
        {"message": "Authenticated!", "user": request.user.username}, status=200
    )
