from rest_framework import permissions
from projects import models
from projects import viewsets


class IsContributorOrowner(permissions.BasePermission):
    """
    Project-level permission to only allow contributors of a project to edit it.
    """

    def has_permission(self, request, view):
        # Permission check before applying has_object_permission or when listing objects.
        if type(view) == viewsets.ProjectViewSet:
            return True
        else:
            project = models.Projects.objects.get(pk=view.kwargs["project_pk"])
            if request.user == project.author_user_id:
                return True
            contributors = models.Contributors.objects.filter(
                user_id=request.user, project_id=project.id
            )
            if contributors:
                return True

    def has_object_permission(self, request, view, obj):
        # Allow object owner to perform all CRUD actions
        if request.user == obj.author_user_id:
            return True

        #  If object type is Project :
        if type(obj) == models.Projects:
            contributors = models.Contributors.objects.filter(
                user_id=request.user, project_id=obj.id
            )
            if contributors:
                if request.method in permissions.SAFE_METHODS:
                    return True

        # If object type is Issue :
        if type(obj) == models.Issues:
            if (
                request.user == obj.project_id.author_user_id
                and request.method in permissions.SAFE_METHODS
            ):
                return True
            contributors = models.Contributors.objects.filter(
                user_id=request.user, project_id=obj.project_id
            )
            if contributors:
                if request.method in permissions.SAFE_METHODS:
                    return True

        # If object type is Comment:
        if type(obj) == models.Comments:
            if (
                request.user == obj.issue_id.project_id.author_user_id
                and request.method in permissions.SAFE_METHODS
            ):
                return True
            contributors = models.Contributors.objects.filter(
                user_id=request.user, project_id=obj.issue_id.project_id
            )
            if contributors:
                if request.method in permissions.SAFE_METHODS:
                    return True
