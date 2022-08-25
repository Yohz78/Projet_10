from django.db import models


class Projects(models.Model):
    """Projects model. Use to save a project."""

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=128, blank=True)

    @property
    def project_id(self):
        return self.id


# class Contributors(models.Model):
#     """Contributors model. Link an user to a project."""

#     CHOICES = {("allowed", "Autorisé")}

#     user_id = models.IntegerField()
#     project_id = models.IntegerField()
#     permission = models.CharField(max_length=150, choices=CHOICES)


# class Issues(models.Model):
#     """Issues model. Allow creation of an issue."""

#     title = models.CharField(max_length=128)
#     desc = models.CharField(max_length=128)
#     tag = models.CharField(max_length=128)
#     priority = models.CharField(max_length=128)
#     project_id = models.IntegerField()
#     status = models.CharField(max_length=128)
#     created_time = models.DateTimeField(auto_now_add=True)


# class Comments(models.Model):
#     """Comments model. Allow creation of comments on an issue."""

#     project_id = models.IntegerField()
#     description = models.TextField(max_length=2048, blank=True)
#     created_time = models.DateTimeField(auto_now_add=True)
