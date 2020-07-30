from django.core.cache import cache
from django.db import models


# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id :
            return super().save()
        else:
            key = f"user{self.id}"
            cache.delete(key)
            return super().save()

    # def save(self, **kwargs):
    #     key = self.id
    #     if key:
    #         cache.delete(key)
    #     super().save(**kwargs)

    def delete(self, **kwargs):
        key = self.id
        cache.delete(key)
        return super().delete()



