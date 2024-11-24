from django.db import models
from django.template.defaultfilters import slugify #slugify a string for navigating

# Create your models here.


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    topic = models.CharField(max_length=250)
    banner = models.ImageField()
    content = models.TextField()

    country = models.CharField(max_length=100, default='Philippines')
    slug = models.SlugField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug:
            pass
        else:
            self.slug = slugify(self.topic.lower())
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.topic
