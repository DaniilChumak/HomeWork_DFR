from materials.models import Course
from rest_framework.serializers import ModelSerializer


class CourseSerializer(ModelSerializer):
    model = Course
    fields = '__all__'
