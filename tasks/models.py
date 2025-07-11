from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
