from django.db import models


# Create your models here.
class Menu(models.Model):
    name_en = models.CharField(max_length=255, verbose_name="ENG name of menu")
    name_mn = models.CharField(max_length=255, verbose_name="MNG name of menu")

    def __unicode__(self):
        return unicode(self.name_mn)


class Category(models.Model):
    menuID = models.ForeignKey(Menu, verbose_name="related menu")
    name_en = models.CharField(max_length=255, verbose_name="ENG name of cat")
    name_mn = models.CharField(max_length=255, verbose_name="MNG name of cat")

    def __unicode__(self):
       return unicode(self.name_mn)


class Info(models.Model):
    catID = models.ForeignKey(Category, verbose_name="related category")
    title_en = models.CharField(max_length=255, verbose_name="ENG name of item")
    title_mn = models.CharField(max_length=255, verbose_name="MNG name of item")
    published_date = models.TimeField("date published", auto_now=True)
    description = models.TextField(verbose_name="description")

    def __unicode__(self):
       return unicode(self.title_mn)


class Picture(models.Model):
    infoID = models.ForeignKey(Info, verbose_name="info id")
    alt = models.CharField(max_length=255, verbose_name="image name")
    image = models.ImageField(upload_to='image')

    def __unicode__(self):
        return unicode(self.alt)
