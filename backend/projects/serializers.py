from rest_framework import serializers

from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    project_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Projects
        fields = ["title", "description", "type", "project_id"]

    def get_project_id(self, obj):
        if not hasattr(obj, "id"):
            return None
        return obj.project_id
