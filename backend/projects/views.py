from rest_framework import authentication, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermissions
from api.authentication import TokenAuthentication

from .models import Projects, Issues, Comments
from .serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer

# Projects related views.


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    """Display the project list and allow project creation."""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        serializer.save()


class ProjectDetailAPIView(generics.RetrieveAPIView):
    """Display a project"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectUpdateAPIView(generics.UpdateAPIView):
    """Update a project"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


# TO BE WORKED ON ??? Can it work with multiple items ?
class ProjectRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Display a project and allow update if user is the author"""

    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def get_project(self):
        project_id = self.kwargs["pk"]
        return get_object_or_404(Projects, pk=project_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ProjectDestroyAPIView(generics.DestroyAPIView):
    """Delete a project"""

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


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


class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# class ProjectMixinView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):

#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer
#     lookup_field = "pk"

#     def get(self, request, *args, **kwargs):
#         print(args, kwargs)
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(self, request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# def post():
#     return


# class ProjectDeleteAPIView(generics.DeleteAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer


# @api_view(["GET", "POST"])
# def project_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Projects, pk=pk)  # Raise 404 if obj does not exist
#             data = ProjectsSerializer(obj, many=False).data
#             return Response(data)
#         else:
#             # get request -> detail view
#             # list view
#             queryset = Projects.objects.all()
#             data = ProjectsSerializer(queryset, many=True).data
#             return Response(data)

#     if method == "POST":
#         # create an item
#         serializer = ProjectsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)
