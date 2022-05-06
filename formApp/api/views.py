from formApp.models import addStd
from rest_framework import viewsets
from formApp.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = addStd.objects.all()
    serializer_class = UserSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]