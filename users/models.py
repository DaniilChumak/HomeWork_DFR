from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson

"""Добавили модель пользователя"""


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите вашу электронную почту"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите ваш номер телефона",
    )
    city = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите ваш город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


"""Добавили модель платежа"""


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        help_text="Выберите пользователя",
    )
    date_of_payment = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оплаты", blank=True, null=True
    )
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Приобретенный курс",
        help_text="Выберите курс, который покупаете",
    )
    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Приобретенный урок",
        help_text="Выберите урок, который покупаете",
    )
    payment_method = models.CharField(
        max_length=35,
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user}: {self.date_of_payment}, {self.course_paid if self.course_paid else self.lesson_paid}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
