from django.contrib import admin
from django.urls import path
from app.views import hey_view, age_in_view, order_view

urlpatterns = [
    path("hey/<name>", hey_view),
    path("age-in/<int:end>/<int:birthyear>", age_in_view),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", order_view),
    path("admin/", admin.site.urls),
]
