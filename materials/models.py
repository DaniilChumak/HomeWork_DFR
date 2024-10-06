from django.db import models
from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview_image = models.ImageField(
        upload_to="materials/courses/previews/",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Загрузите картинку для превью курса",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Выберите курс",
    )
    preview_image = models.ImageField(
        upload_to="materials/lessons/previews/",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Загрузите картинку для превью курса",
    )
    link_to_video = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        blank=True,
        null=True,
    )
    sign_of_subscription = models.BooleanField(
        default=False,
        verbose_name='Признак подписки'
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.user}: {self.course}'
