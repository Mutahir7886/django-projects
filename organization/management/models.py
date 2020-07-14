from django.db import models

class organizaations(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @property
    def branches(self):
        return self.branches_set.all()


class Branches(models.Model):

    name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    organizaations=models.ForeignKey(organizaations,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.organizaations) + '-' + self.name



class users(models.Model):

    name=models.CharField(max_length=100)
    id_num=models.IntegerField()
    RANK_CHOICES = (
        ('Doc', 'Doctor'),
        ('Adm', 'Admin'),
    )
    Ranks = models.CharField(max_length=10, choices=RANK_CHOICES)

    def __str__(self):
        return str(self.name) + '-' + self.Ranks



class co_relation(models.Model):

    users=models.ForeignKey(users,on_delete=models.CASCADE)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE)



