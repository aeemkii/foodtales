from django.db import models

from apps.accounts.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField("Название",max_length=50)
    slug = models.SlugField(max_length=60)
    icon = models.ImageField(upload_to="category/icons")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField("Название",max_length = 100, unique = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"





class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Фото")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    is_draft = models.BooleanField("Черновик", default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="posts"
                                 )
    tags = models.ManyToManyField(Tag, related_name = "tag_posts")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title