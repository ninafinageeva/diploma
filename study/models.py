from django.db import models
from users.models import User, NULLABLE


class Students(models.Model):
    first_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Фамилия')
    email = models.EmailField(max_length=250, **NULLABLE, unique=True, verbose_name='Адрес электронной почты')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email} - {self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'


class Study(models.Model):
    title = models.CharField(max_length=100, **NULLABLE, verbose_name='название')
    link = models.URLField(**NULLABLE, verbose_name='ссылка на обучение')
    plan = models.CharField(max_length=100, **NULLABLE, verbose_name='план обучения')
    study_start = models.DateField(**NULLABLE, verbose_name='начало обучения')
    student = models.ManyToManyField(Students, **NULLABLE, verbose_name='студент')
    updated_at = models.DateTimeField(verbose_name='время обновления', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.link}'

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучения'


class Materials(models.Model):
    title = models.CharField(max_length=100, verbose_name='название лекции')
    content = models.TextField(**NULLABLE, verbose_name='содержание')
    study_materials = models.ForeignKey(Study, **NULLABLE, on_delete=models.CASCADE, verbose_name='материалы обучения')
    autor = models.CharField(max_length=255, **NULLABLE, verbose_name='автор контента')

    def __str__(self):
        return f'{self.title}: {self.content}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

