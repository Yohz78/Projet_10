from rest_framework.routers import DefaultRouter
from projects.viewsets import ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("comments", CommentViewSet, basename="comments")
router.register("issues", IssueViewSet, basename="issues")

urlpatterns = router.urls
print(urlpatterns)
