from django.urls import path
from calculator.views import recipe, info

urlpatterns = [
    path('omlet/', recipe),
    path('pasta/', recipe),
    path('buter/', recipe),
    path('', info),
]

handler404 = "calculator.views.page_not_found_view"