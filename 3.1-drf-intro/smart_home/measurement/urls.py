from django.urls import path
from .views import CreateProject, UpdateProject, MeasurementProject, ListProject, RetrieveProject

urlpatterns = [
    path('create/', CreateProject.as_view()),
    path('update/', UpdateProject.as_view()),
    path('measurement/', MeasurementProject.as_view()),
    path('list/', ListProject.as_view()),
    path('retrieve/<pk>/', RetrieveProject.as_view())

    # TODO: зарегистрируйте необходимые маршруты
]
