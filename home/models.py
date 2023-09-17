from django.db import models

class Grade(models.Model):
    grade = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.grade

class Grade_sub(models.Model):
    grade  = models.ForeignKey(Grade,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.sub_name

class Content(models.Model):
    sub_name = models.ForeignKey(Grade_sub,on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    Content = models.TextField()


    def __str__(self) -> str:
        return f"{self.sub_name.sub_name}|{self.sub_name.grade.grade}|{self.title}"



