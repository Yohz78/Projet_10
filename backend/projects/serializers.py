from rest_framework import serializers

from .models import Projects, Issues, Comments


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["pk", "title", "description", "type", "project_id"]


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = [
            "pk",
            "title",
            "desc",
            "tag",
            "priority",
            "project_id",
            "status",
            "created_time",
        ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "pk",
            "project_id",
            "description",
            "created_time",
        ]
