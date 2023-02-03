from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import CookieStand
from .serializer import CookieStandSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    queryset = CookieStand.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CookieStandSerializer
