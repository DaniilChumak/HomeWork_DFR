from materials.models import Course, Lesson
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_count', 'lessons')

