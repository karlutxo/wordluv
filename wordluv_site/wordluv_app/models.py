from django.db import models
from django.urls import reverse


class word(models.Model):
    word = models.CharField(max_length=25)
    meaning = models.TextField()
    examples = models.TextField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
         return format(self.id) + "   " + self.word + " .-  " + self.meaning
         
    def get_absolute_url(self):
        return reverse("worddetailSlug", kwargs={"slug": self.slug})
