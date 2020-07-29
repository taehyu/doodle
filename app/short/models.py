from hashlib import md5

from django.db import models


# Create your models here.


class Short(models.Model):
    input_url = models.URLField()
    output_url = models.URLField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.output_url = md5(self.input_url.encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)

