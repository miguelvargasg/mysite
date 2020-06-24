from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blogs_posts',
        null=False
    )

    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible'
    )

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )

    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',
    )

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )

    def publish(self):
        self.status = self.PUBLISHED
        self.published = timezone.now()

    objects = PostQuerySet.as_manager()

def __str__(self):
    return self.name
    return self.title
