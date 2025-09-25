from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version="v1",
        description="API documentation for E-Commerce Backend",
        contact=openapi.Contact(email="youremail@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", lambda request: redirect("dashboard_home", permanent=False)),

    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),

    # Users
    path("signup/", include("users.urls")),           
    path("api/users/", include("users.api_urls")),    

    path("api/products/", include("products.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/carts/", include("carts.urls")),

    # JWT Authentication
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Swagger & Redoc
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
