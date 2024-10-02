from materials.models import Course, Lesson
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson_in_course = SerializerMethodField()

    def get_count_lesson_in_course(self, course):
        return Course.object.filter(Lesson=course.lesson).count()

    class Meta:
        model = Course
        fields = ("title", "preview_image", "description", "count_lesson_in_course")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
