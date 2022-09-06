from django.db import models

class word(models.Model):
    word = models.CharField(max_length=25)
    meaning = models.TextField()
    examples = models.TextField(null=True)

    def __str__(self):
         return self.word + " .-  " + self.meaning