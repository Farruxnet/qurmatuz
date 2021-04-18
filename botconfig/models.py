from django.db import models
from django.utils.html import format_html
from django.utils import timezone

class Messages(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now, verbose_name='Qo\'shilgan vaqti')
    def __str__(self):
        return self.text


class StartNarx(models.Model):
    narx = models.CharField(max_length=50, verbose_name='Boshlang\'ich narx')
    def __str__(self):
        return str(self.narx)
    class Meta:
        verbose_name = "Boshlang\'ich narxlar"
        verbose_name_plural = "Boshlang\'ich narxlar"

class Config(models.Model):
    text = models.TextField(verbose_name='Start matni')
    about = models.TextField(verbose_name='Haqida')
    contact = models.TextField(verbose_name='Aloqa ma\'lumotlari')
    list_count = models.IntegerField(default=5, verbose_name='E\'lonlar ro\'yxat soni')
    whouse = models.TextField(verbose_name='Qanday foydalaniladi?')
    CHOICES = (
        ('oz', 'O\'zbek'),
        ('uz', 'Узбек'),
        ('ru', 'Руский'),
    )
    lan = models.CharField(choices=CHOICES, max_length=30)
    class Meta:
        verbose_name = "Bot sozlamalari"
        verbose_name_plural = "Bot sozlamalari"
    def __str__(self):
        return self.text

class Viloyat(models.Model):
    oz = models.CharField(max_length=80, unique=True, verbose_name='O\'zbek')
    uz = models.CharField(max_length=80, unique=True, verbose_name='Krill')
    ru = models.CharField(max_length=80, unique=True, verbose_name='Rus')
    status = models.BooleanField(default=False, verbose_name='Holati')
    def __str__(self):
        return self.oz
    class Meta:
        verbose_name = "Viloyatlar"
        verbose_name_plural = "Viloyatlar"



class Tuman(models.Model):
    oz = models.CharField(max_length=80, unique=True, verbose_name='O\'zbek')
    uz = models.CharField(max_length=80, unique=True, verbose_name='Krill')
    ru = models.CharField(max_length=80, unique=True, verbose_name='Rus')
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, verbose_name='Viloyatni tanlang')

    def __str__(self):
        return self.oz
    class Meta:
        verbose_name = "Tumanlar"
        verbose_name_plural = "Tumanlar"

class AvtoKub(models.Model):
    kub = models.CharField(max_length=10, verbose_name='Avtomobil sig\'imi')
    def __str__(self):
        return str(self.kub)
    class Meta:
        verbose_name = "Avtomobil sig\'imi"
        verbose_name_plural = "Avtomobil sig\'imi"

class Avto(models.Model):
    oz = models.CharField(max_length=80, unique=True, verbose_name='O\'zbek')
    uz = models.CharField(max_length=80, unique=True, verbose_name='Krill')
    ru = models.CharField(max_length=80, unique=True, verbose_name='Rus')
    def __str__(self):
        return self.oz
    kub = models.ManyToManyField(AvtoKub, verbose_name='Avtomobil sig\'imi. bir nechta tanlash mumkin ctrl tugamsini bosgan holatda.')
    class Meta:
        verbose_name = "Avtomobillar"
        verbose_name_plural = "Avtomobillar"

class Category(models.Model):
    oz = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='O\'zbek')
    uz = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='Krill')
    ru = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='Rus')

    def __str__(self):
        return str(self.oz)
    class Meta:
        verbose_name = "Bo\'limlar"
        verbose_name_plural = "Bo\'limlar"


class PodCategory(models.Model):
    oz = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='O\'zbek')
    uz = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='Krill')
    ru = models.CharField(max_length=80, null=True, blank=True, unique=True, verbose_name='Rus')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Bo\'limni tanlang')
    def __str__(self):
        return self.oz
    class Meta:
        verbose_name = "Kichik bo\'limlar (podkategoryalar)"
        verbose_name_plural = "Kichik bo\'limlar (podkategoryalar)"

class Paket(models.Model):
    name_oz = models.CharField(max_length=80, unique=True, verbose_name='O\'zbek')
    name_uz = models.CharField(max_length=80, unique=True, verbose_name='Krill')
    name_ru = models.CharField(max_length=80, unique=True, verbose_name='Rus')
    day = models.IntegerField(default=0, verbose_name='Amal qilish vaqti (kun)')
    price = models.IntegerField(verbose_name='Narxi (sum)')

    def __str__(self):
        return self.name_oz
    class Meta:
        verbose_name = "Tariflar (paket)"
        verbose_name_plural = "Tariflar (paket)"




#################3
