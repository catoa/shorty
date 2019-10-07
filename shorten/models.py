from django.db import models
from django.shortcuts import reverse


class ShortenedUrl(models.Model):
    url = models.URLField(blank=False)
    shortened_id = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("shorten:reroute", kwargs={"shortened_id": self.shortened_id})

    def __str__(self):
        return f"Id: {self.shortened_id} - {self.created_at!s}"
