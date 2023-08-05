from django.db import models
from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

class Post(models.Model):
    title = models.CharField(max_length=250,)
    image = models.ImageField(upload_to='images/post', blank=True, null=True)
    descrip  = models.TextField()
    data = models.DateField(auto_now=timezone.now())
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Роли'
        verbose_name = 'Роль'
    
class Members(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/members', blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    insta_link = models.CharField(max_length=300)
    git_link = models.CharField(max_length=300)
    tg_link = models.CharField(max_length=300)
    port_link = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Мемберы'
        verbose_name = 'Мембер'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'




