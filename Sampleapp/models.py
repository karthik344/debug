from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=35,null=True)
    esal = models.IntegerField(default=0.0)
    eaddress = models.CharField(max_length=35)
    Designation = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural ='EmployeesInformation'

    def __str__(self):
        return self.ename + "------" +self.Designation
