from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    store = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
