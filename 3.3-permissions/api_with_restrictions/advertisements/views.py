from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import CanDelUpd
from advertisements.serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = AdvertisementFilter.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update"]:
            return [CanDelUpd()]
        if self.request.method == "DELETE":
                return [CanDelUpd()]
        return []
