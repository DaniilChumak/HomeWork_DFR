from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import (
    CourseViewSet,
    LessonListAPIView,
    LessonDestroyAPIView,
    LessonRetrieveAPIView,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    SubscriptionCreateApiView,
)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path('course_subscription/', SubscriptionCreateApiView.as_view(), name='course_subscription'),
]

urlpatterns += router.urls
