from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Item(models.Model):
    in_stock = (
        ('No', 'Нет в наличии'),
    )
    item_title = models.CharField("Наименование товара", max_length=250, blank=False)
    item_features = RichTextField("Характеристики")
    amount = models.IntegerField("Количество")
    price = models.IntegerField("Цена", blank=True, null=True)
    item_photo = models.ImageField("Фото товара", upload_to='photos/%Y/%m/%d/')
    description = RichTextField("Описание")
    is_in_stock = models.CharField("Есть ли в наличии?", choices=in_stock,max_length=100, blank=True, null=True)
    is_popular = models.BooleanField("Популярный товар", default=False)
    is_contract_price = models.BooleanField("Договорная цена", default=False)
    created_date = models.DateTimeField("Дата", default=datetime.now, blank=True)

    def __str__(self):
        return self.item_title
