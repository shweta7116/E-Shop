from django.contrib import admin
from .models import *
from django.urls import reverse
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['image_tag','cat_id','title','add_date']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= [ 'image','id','title','selling_price','discounted_price','discription','brand','category','image_tag','product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','customer','customer_info' ,'product','product_info' ,'quantity','ordered_date','status']

    def customer_info(self,obj):
        link = reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html( '<a href="{}">{}</a>',link,obj.customer.name)

    def product_info(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html( '<a href="{}">{}</a>',link,obj.product.title)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'status':
            kwargs['choices'] = (
                 ('Accepted','Accepted'),
                ('Packed','Packed'),
                ('OnTheWay','On-The-Way'),
                ('Delivered','Delivered'),
                ('Cancle','Cancle'),
            )
            if request.user.is_superuser:
                kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)


