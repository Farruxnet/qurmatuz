from django.db import models
from botconfig.models import Avto, AvtoKub, Category, PodCategory, Tuman, Viloyat, StartNarx, Paket
import datetime
from django.utils import timezone
class TgUser(models.Model):
    tg_id = models.IntegerField()
    name = models.CharField(max_length=50)
    lan = models.CharField(max_length=25)
    step = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"
    def __str__(self):
        return self.name

class UserSearch(models.Model):
    tg_id = models.IntegerField()
    category = models.CharField(max_length=50, null=True)
    podcategory = models.CharField(max_length=50, null=True)
    avto = models.CharField(max_length=50, null=True)
    avtokub = models.CharField(max_length=50, null=True)
    viloyat = models.CharField(max_length=50, null=True)
    tuman = models.CharField(max_length=50, null=True)


class UserCart(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Bo\'lim')
    narx = models.ForeignKey(StartNarx,  blank=True, help_text="--------- belgi kelishilgan narx", null=True, on_delete=models.CASCADE, verbose_name='Boshlang\'ich narx')
    podcategory = models.ForeignKey(PodCategory, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Podkategoryalar')
    avto = models.ForeignKey(Avto, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Avtomobil')
    kub = models.ForeignKey(AvtoKub, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Avtomobil sig\'imi')
    viloyat = models.ForeignKey(Viloyat, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Viloyatlar')
    tuman = models.ForeignKey(Tuman, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Tumanlar')
    telefon = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefon raqam')
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telegram username')
    paket = models.ForeignKey(Paket, blank=True, on_delete=models.CASCADE, null=True, verbose_name='Tarif')
    date = models.DateTimeField(default=timezone.now, verbose_name='Qo\'shilgan vaqti')
    deatline = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=1), verbose_name='Amal qilish vaqti')
    status = models.BooleanField(default=False, verbose_name='Holati')
    status_check = models.BooleanField(default=False, verbose_name='To\'liq emas e\'lon')

    class Meta:
        verbose_name = "Foydalanuvchilar e\'lonlari"
        verbose_name_plural = "Foydalanuvchilar e\'lonlari"
        ordering = ['id']
    def __str__(self):
        return str(self.user)




















###################
