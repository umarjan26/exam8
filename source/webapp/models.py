from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
STATUS_CHOICES = [('toys', 'игрушки'), ('cars', 'машина'), ('phone', 'телефон'), ('clothes', 'одежда')]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(max_length=100,
                                choices=STATUS_CHOICES,
                                default=STATUS_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.TextField(max_length=2000, verbose_name='Описание', null=True, blank=True)


    def __str__(self):
        return f'{self.pk}.{self.name} - {self.category}'

    class Meta:
        db_table = 'Products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def average(self):
        reviews = self.reviews.filter(status=True)
        sum = 0
        if reviews:
            for review in reviews:
                sum += review.grade
            return round(sum / len(reviews), 2)
        else:
            return 0


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               default=1,
                               verbose_name='Автор',
                               related_name='reviews')
    product = models.ForeignKey('webapp.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='reviews')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    grade = models.IntegerField(verbose_name='Оценка')
    status = models.BooleanField(verbose_name='Статус', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return f'{self.pk}.{self.grade} - {self.author.username}'

    class Meta:
        db_table = 'Reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        permissions = [
            ('can_view_false_reviews', 'Может видеть все не модерированные отзывы')
        ]