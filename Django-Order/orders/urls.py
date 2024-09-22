from django.urls import path
from .views import top_customers_view, create_users_view, test_auth_view

urlpatterns = [
    path("create-users", create_users_view, name="create_users"),
    path("top-customers", top_customers_view, name="top_customers"),
    path("test-auth", test_auth_view, name="test-auth"),
]
