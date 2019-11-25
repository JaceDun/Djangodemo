from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()


class Account(models.Model):
    name = models.CharField('会员号', max_length=50, unique=True)
    pwd = models.CharField('姓名', max_length=100)
    email = models.EmailField('电子邮箱')
    phone = models.CharField('电话', max_length=100)


def __unicode__(self):
    return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
