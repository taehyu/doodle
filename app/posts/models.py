from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('rough_draft', 'Rough Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rough_draft')

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


