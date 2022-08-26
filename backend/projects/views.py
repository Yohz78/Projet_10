from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermissions

from .models import Projects
from .serializers import ProjectsSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        serializer.save()


project_list_create_view = ProjectListCreateAPIView.as_view()


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    permission_classes = [permissions.DjangoObjectPermissions]
    serializer_class = ProjectsSerializer


class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"
    permission_classes = [permissions.DjangoObjectPermissions]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProjectMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(self, request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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
