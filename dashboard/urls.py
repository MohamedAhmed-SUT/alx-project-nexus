from django.urls import path
from . import views

urlpatterns = [
    # ================= Dashboard Home =================
    path('', views.admin_dashboard, name="dashboard_home"),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('reports/', views.reports_view, name='reports_view'),

    # ================= User Management =================
    path('users/', views.users_list, name="users_list"),
    path('users/<int:pk>/role/', views.user_update_role, name="user_update_role"),
    path('users/<int:pk>/delete/', views.admin_user_delete, name="user_delete"),  # استخدم الدالة الخاصة بالمستخدمين

    # ================= Authentication =================
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),

    # ================= Profile & Settings =================
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('password/change/', views.password_change, name='password_change'),

    # ================= Products (Admin Only) =================
    path('products/', views.products_list, name='products_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # ================= Orders =================
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('orders/export/csv/', views.export_orders_csv, name='export_orders_csv'),

    # ================= Cart =================
    path('cart/', views.cart_page, name='cart_page'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    #===============shop================
    path('shop/', views.shop_view, name='shop'),

]
