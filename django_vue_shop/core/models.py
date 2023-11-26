import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
        

class Category(models.Model):
    name = models.CharField(max_length=155)
    discription = models.TextField()

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=155)
    discription = models.TextField()

    def __str__(self):
        return self.name

class Game(models.Model):

    class TypeProduct(models.TextChoices):
        GAMES = 'G', _('GAMES')
        DLC = 'D', _('ADDITIONS')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=155)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    # subcategory = models.ManyToManyField(Subcategory, related_name='subcategory')
    discription = models.TextField()
    price = models.IntegerField()
    relized_by = models.CharField(max_length=300)
    link_creator = models.SlugField()
    relized_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GameDl(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=155)
    discription = models.TextField()
    price = models.IntegerField()
    link_creator = models.SlugField()
    relized_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    recommendation = models.BooleanField(default=True)
    relized_by = models.CharField(max_length=300)
    relized_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.game) + ' | ' + str(self.relized_by)

class SubReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField()
    relized_by = models.CharField(max_length=300)
    relized_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'subreview:' + str(self.review.game) + ' | ' + str(self.review.relized_by)

# class SystemRequirement(models.Model):
#     class OS(models.TextChoices):
#         LINUX = 'L', _('Linux')
#         WINDOWS = 'W', _('Windows')
#         MACOS = 'M', _('MacOS')
#         PS = 'P', _('PlayStation')
#         XBOX = 'X', _('XBox')

#     class TypeRequirements(models.TextChoices):
#         MINIMUM = 'M', _('Minimals')
#         RECOMMEND = 'R', _('Recommends')

#     id = models.UUIDField('UUID продукта',
#                           primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False)

#     operating_system = models.CharField('ОС',
#                                         max_length=2,
#                                         choices=OS.choices,
#                                         help_text='Укажите ОС')

#     game = models.ForeignKey(Game,
#                                 on_delete=models.CASCADE,
#                                 related_name='system_requirements',
#                                 limit_choices_to={
#                                     'type': Game.TypeProduct.GAMES})

#     device_processor = models.CharField('Процессор',
#                                         max_length=100,
#                                         help_text='Укажите процессор')

#     device_memory = models.CharField('Колличество ОЗУ',
#                                      max_length=100,
#                                      help_text='Укажите колличество ОЗУ')

#     device_storage = models.CharField('Колличество памяти на Диске',
#                                       max_length=100,
#                                       help_text='Укажите колличество памяти на Диске')

#     device_graphics = models.CharField(
#         'Модель видеокарты и колличество памяти',
#         max_length=100,
#         help_text='Укажиет модель видеокарты и колличество памяти')

#     type_requirements = models.CharField('Тип системных требований',
#                                          max_length=2,
#                                          choices=TypeRequirements.choices,
#                                          help_text='Укажите тип системных требований')

#     def __str__(self):
#         return self.type_requirements

#     class Meta:
#         db_table = 'system_requirement'
#         verbose_name = 'системная характеристика'
#         verbose_name_plural = 'системные характеристики'



