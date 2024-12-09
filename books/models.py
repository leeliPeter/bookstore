from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,  # Allow null temporarily
        blank=True  # Allow blank temporarily
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
