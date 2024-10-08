from materials.models import Course, Lesson, Subscription
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.validators import LinkToVideoValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkToVideoValidator(field="link_to_video")]


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")
    subscription = SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ("title", "description", "lesson_count", "lessons", "subscription")


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)
