from django.db import models
from django.utils.dateformat import DateFormat


class Employee(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)
    mail = models.EmailField(max_length=254)
    working_place = models.CharField(max_length=50)
    WORKING_CONTRACT = (
        ('CDD', 'CDD'),
        ('CDI', 'CDI'),
        ('CDD_CDI', 'CDD-CDI'),
        ('INTERIM', 'Interim'),
        ('REP', 'Replacement'),
        ('ALE', 'ALE'),
        ('UNDEFINED', 'Undefined'),
    )
    working_contract = models.CharField(max_length=8, choices=WORKING_CONTRACT)
    WORKING_SCHEDULE = (
        ('EXTRA', 'Extra School Schedule'),
        ('MIDDAY', 'Midday Schedule'),
        ('FULL', 'Full Time Schedule'),
        ('UNDEFINED', 'Undefined'),
    )
    working_schedule = models.CharField(max_length=8, choices=WORKING_CONTRACT)
    working_task = models.CharField(max_length=200)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class Row(models.Model):
    emp_abs = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="absent employee",
        related_name="emp_abs",
    )
    emp_rep = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="replacement employee",
        related_name="emp_rep",
    )
    date_from = models.DateTimeField('date from')
    date_to = models.DateTimeField('date to')
    absence_reason = models.CharField('absence reason', max_length=200)

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.emp_abs, self.emp_rep, DateFormat(self.date_from).format('j/m/Y H:i:s'), DateFormat(self.date_to).format('j/m/Y H:i:s'), self.absence_reason)