from rest_framework import generics

from .models import Projects
from .serializers import ProjectsSerializer


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        serializer.save()


project_create_view = ProjectCreateAPIView.as_view()


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectListAPIView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
