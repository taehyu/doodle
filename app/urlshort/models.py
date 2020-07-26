import re
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
import string
import time


class UrlShort(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shorteners', null=True)
    url_bf = models.URLField(null=False)
    url_af = models.URLField(max_length=200, default="")
    count = models.PositiveIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # self.long_to_short()
        self.not_duplicated = True
        if self.count == 0 :
            self.url_af = self.uuid_long_to_short()
            if self.not_duplicated:
                super().save()
        else :
            super().save()

    def uuid_long_to_short(self):
        for i in range(5):
            short_url = 'http://127.0.0.1:8000/happy/' + uuid4().hex[:6]
            # short_url = 'http://127.0.0.1:8000/happy/cute' # 중복 체크
            is_short_url = UrlShort.objects.filter(url_af=short_url).exists()
            if not is_short_url:
                return short_url
        else:
            print("중복 5회 이상! ")
            self.not_duplicated = False