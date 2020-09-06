from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')  # 다대 다 관계처리
    # 외래키가 바라보는 값이 삭제될 때 외래키 필드를 포함하는 모델 인스턴스(row)도 같이 삭제한다.
    Publisher = models.ForeignKey('publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return
