from django.db import models
from django.conf import settings


def upload_diary_image(instance, filename):
    return f"/home/abhi102/diaryapi/static_cdn/media_root/{instance.user}/{filename}"


class DiaryQuerySet(models.QuerySet):
    pass


class DiaryManager(models.Manager):
    def get_queryset(self):
        return DiaryQuerySet(self.model, using=self._db)


class Diary(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    image = models.ImageField(
        upload_to=upload_diary_image, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = DiaryManager()

    def __str__(self):
        return self.title

    @property
    def owner(self):
        return self.user

    class Meta:
        verbose_name = "Diary Post"
        verbose_name_plural = "Diary Posts"
