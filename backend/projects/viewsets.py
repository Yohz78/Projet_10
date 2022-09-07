from rest_framework import viewsets
from api import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Issues, Comments, Contributors
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
    permission_classes = [permissions.IsContributorOrowner, IsAuthenticated]
    lookup_field = "pk"

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author_user_id=author)


class IssueViewSet(viewsets.ModelViewSet):
    """Issues ViewSet"""

    serializer_class = IssuesSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.IsContributorOrowner,
    ]

    def get_queryset(self):
        project = self.kwargs["project_pk"]
        return Issues.objects.filter(project_id=project)

    def perform_create(self, serializer):
        project_id = self.kwargs["project_pk"]
        project = Projects.objects.filter(pk=project_id)[0]
        author = self.request.user
        serializer.save(author_user_id=author, project_id=project)


class CommentViewSet(viewsets.ModelViewSet):
    """Comments ViewSet"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.IsContributorOrowner,
    ]
    lookup_field = "pk"

    def get_queryset(self):
        issue = self.kwargs["issue_pk"]
        return Comments.objects.filter(issue_id=issue)

    def perform_create(self, serializer):
        issue_id = self.kwargs["issue_pk"]
        issue = Issues.objects.filter(pk=issue_id)[0]
        author = self.request.user
        serializer.save(author_user_id=author, issue_id=issue)


class ContributorViewSet(viewsets.ModelViewSet):
    """Contributor ViewSet"""

    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.IsProjectOwner,
    ]
    lookup_field = "pk"

    def perform_create(self, serializer):
        project_id = self.kwargs["project_pk"]
        project = Projects.objects.filter(pk=project_id)[0]
        serializer.save(project_id=project)
