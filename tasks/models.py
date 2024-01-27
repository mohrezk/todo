from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    review = models.DateField(null=True, blank=True)

    
    def __str__(self):
        return self.title
    
    # def review_time()