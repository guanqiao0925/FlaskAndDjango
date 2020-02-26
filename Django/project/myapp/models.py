from django.db import models


# Create your models here.


# 班级模型
class Grades(models.Model):
    gname    = models.CharField(max_length=24)
    ggirl    = models.ImageField()
    gboy     = models.ImageField()
    isDelete = models.BooleanField(default=False)

    def __repr__(self):
        return self.gname


# 学生模型
class Students(models.Model):
    sname    = models.CharField(max_length=24)
    sgender  = models.BooleanField(default=True)
    sage     = models.ImageField()
    isDelete = models.BooleanField(default=False)

    # 关联外键
    sgrade   = models.ForeignKey('Grades', on_delete=models.CASCADE)

    def __repr__(self):
        return self.sname