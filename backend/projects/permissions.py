from rest_framework import permissions


class IsStaffEditorPermissions(permissions.DjangoObjectPermissions):

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
    # user = request.user
    # print(user.get_all_permissions())
    # if request.user.is_staff:
    #     if user.has_perm("projects.add_projects"):
    #         return True
    #     if user.has_perm("projects.change_projects"):
    #         return True
    #     if user.has_perm("projects.delete_projects"):
    #         return True
    #     if user.has_perm("projects.view_projects"):
    #         return True
    #     return False
    # return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.author_user_id == request.user


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user
