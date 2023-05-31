from django.db import models

class TeamModel(models.Model):
    ful_name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='image/')
    subject = models.CharField(max_length=100)
    telegram = models.URLField('Your telegram profile')
    instagram = models.URLField('Your instagram profile',blank=True)
    github = models.URLField('Your GitHub profile')
    email = models.EmailField('Your Email')


    def __str__(self):
        return self.ful_name

class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='img')
    text = models.TextField(max_length=1000)
    datatime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class InfoNewsModel(models.Model):
    title = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='img')
    text = models.TextField(max_length=1000)
    img2 = models.ImageField(upload_to='img')
    img3 = models.ImageField(upload_to='img',blank=True)
    new = models.ForeignKey(NewsModel,models.CASCADE)

    def __str__(self) -> str:
        return self.title