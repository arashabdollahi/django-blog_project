from django.db import models
from django.shortcuts import reverse
class Post (models.Model):
    STATUS_CHOICE = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_time_create = models.TimeField(auto_now_add=True)
    date_time_modified = models.TimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=3)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
    


