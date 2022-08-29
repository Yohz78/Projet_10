from rest_framework import viewsets
from .models import Projects, Issues, Comments
from .serializers import IssuesSerializer, ProjectsSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"
