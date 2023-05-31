from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    

class TeacherModell(models.Model):
    img = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)
    choise = (
        ('katta','oqituvchi'),
        ('dotsent','dotsent'),
        ('professor','professor'),
        ('assistent','assistent')
    )
    teacher23 = models.CharField(max_length=214,choices=choise)

    def __str__(self):
        return self.name



class InfoModell(models.Model):
    img = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    rate = models.CharField(max_length=50)
    document = models.FileField(upload_to='pdf')
  

    def __str__(self):
        return self.name

class DocumentModel(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='pdf')
    types = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title