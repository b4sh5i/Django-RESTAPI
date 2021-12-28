from rest_framework import viewsets
from .serializers import NodeSerializer
from .models import Node
from rest_framework import permissions

# Create your views here.
class NodeView(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)