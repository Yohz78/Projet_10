from rest_framework import authentication, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermissions
from api.authentication import TokenAuthentication

from .models import Projects, Issues, Comments
from .serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer


#  To check : Can we use the same view for differents items ? Depending on permissions ?
# Projects related views.


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    """Display the project list and allow project creation."""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):
    """Display a project"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    """Display a project and allow deletion"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"


class ProjectRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Display a project and allow update if user is the author"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"


# Issues related views.


class IssueListCreateAPIView(generics.ListCreateAPIView):
    """Display the issues list and allow issue creation."""

    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        serializer.save()


class IssueDetailAPIView(generics.RetrieveAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer


class IssueUpdateAPIView(generics.UpdateAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


class IssueDestroyAPIView(generics.DestroyAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# Same as Projects. To be worked on and tested extensively.
class IssueRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Display a project and allow update if user is the author"""

    serializer_class = IssuesSerializer
    lookup_field = "pk"


# Comments related views.


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """Display the issues list and allow issue creation."""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        serializer.save()


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# Same as Projects. To be worked on and tested extensively.
class CommentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Display a project and allow update if user is the author"""

    serializer_class = CommentsSerializer
    lookup_field = "pk"
