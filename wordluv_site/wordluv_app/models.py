from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class word(models.Model):
    word = models.CharField(max_length=25)
    meaning = models.TextField()
    examples = models.TextField(null=True)
    slug = AutoSlugField(populate_from='word')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    lastshown = models.DateTimeField(null=True)

    def __str__(self):
         return format(self.id) + "   " + self.word + " .-  " + self.meaning
         
    def get_absolute_url(self):
        return reverse("worddetailSlug", kwargs={"slug": self.slug})
