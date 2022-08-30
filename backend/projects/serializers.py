from rest_framework import serializers

from .models import Projects, Issues, Comments, Contributors
from django.contrib.auth.models import User


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["pk", "title", "description", "type"]


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
            "issue_id",
            "description",
            "created_time",
        ]


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["pk", "permission", "project_id", "user_id"]
