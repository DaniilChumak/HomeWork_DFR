from rest_framework.serializers import ValidationError


"""Валидатор проверки ссылок в материалах"""
class LinkToVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = "http://youtube.com"
        if value.get("link_to_video"):
            if link not in value.get("url_video"):
                raise ValidationError("Можно добавлять только ссылки на youtube.")
