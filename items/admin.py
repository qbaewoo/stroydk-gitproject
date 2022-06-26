from django.contrib import admin
from . models import Item
from django.utils.html import format_html
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.item_photo.url))

    thumbnail.short_description = 'Фото товара'
    list_display = ('id', 'thumbnail', 'item_title', 'amount', 'price', 'is_in_stock', 'is_popular', 'is_contract_price')
    list_display_links = ('id','thumbnail', 'item_title')
    list_editable = ('is_popular', 'is_contract_price')
    search_fields = ('id','item_title')
    list_filter = ('is_in_stock','is_popular','is_contract_price')

admin.site.register(Item, ItemAdmin)
