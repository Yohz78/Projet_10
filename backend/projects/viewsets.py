from rest_framework import viewsets
from .models import Projects, Issues, Comments, Contributors
from django.contrib.auth.models import User
from .serializers import (
    IssuesSerializer,
    ProjectsSerializer,
    CommentsSerializer,
    ContributorsSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    """Projects ViewSet"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author_user_id=author)


class IssueViewSet(viewsets.ModelViewSet):
    """Issues ViewSet"""

    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author_user_id=author)


class CommentViewSet(viewsets.ModelViewSet):
    """Comments ViewSet"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author_user_id=author)


class ContributorViewSet(viewsets.ModelViewSet):
    """Contributor ViewSet"""

    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    lookup_field = "pk"
