# Generated by Django 4.1 on 2022-09-02 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0004_alter_issues_priority_alter_projects_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="comments",
            name="description",
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="comments",
            name="issue_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="projects.issues"
            ),
        ),
        migrations.AlterField(
            model_name="contributors",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="projects.projects"
            ),
        ),
        migrations.AlterField(
            model_name="contributors",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="projects.projects"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
