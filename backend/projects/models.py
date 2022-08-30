from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Projects(models.Model):
    """Projects model. Use to save a project."""

    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=128, blank=True)


class Issues(models.Model):
    """Issues model. Allow creation of an issue."""

    CHOICES = {("1", "Faible"), ("2", "Moyenne"), ("3", "Elevée")}

    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=150, choices=CHOICES)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class Comments(models.Model):
    """Comments model. Allow creation of comments on an issue."""

    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, blank="true")
    description = models.TextField(max_length=2048, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class Contributors(models.Model):
    """Contributors model. Link an user to a project."""

    CHOICES = {("allowed", "Autorisé")}

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    permission = models.CharField(max_length=150, choices=CHOICES)
