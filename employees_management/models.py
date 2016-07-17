# -*- coding: utf-8 -*-
from django.db import models
from django.utils.dateformat import DateFormat
from django.utils.translation import ugettext_lazy as _


class Employee(models.Model):
    first_name = models.CharField(_(u'Firstname'), max_length=30)
    last_name = models.CharField(_(u'Lastname'), max_length=30)
    street = models.CharField(_(u'Street'), max_length=100)
    mobile_number = models.CharField(_(u'Mobile Number'), max_length=12)
    phone_number = models.CharField(_(u'Phone Number'), max_length=12)
    mail = models.EmailField(_(u'Mail'), max_length=254)
    working_place = models.CharField(_(u'Working Place'), max_length=50)
    WORKING_CONTRACT = (
        ('CDD', _(u'CDD')),
        ('CDI', _(u'CDI')),
        ('CDD_CDI', _(u'CDD-CDI')),
        ('INT', _(u'Interim')),
        ('REP', _(u'Replacement')),
        ('ALE', _(u'ALE')),
        ('UND', _(u'Undefined')),
    )
    working_contract = models.CharField(_(u'Working Contract'), max_length=7, choices=WORKING_CONTRACT, default='UND')
    WORKING_SCHEDULE = (
        ('EXTRA', _(u'Extra School Schedule')),
        ('MIDDAY', _(u'Midday Schedule')),
        ('FULL', _(u'Full Time Schedule')),
        ('UND', _(u'Undefined')),
    )
    working_schedule = models.CharField(_(u'Working Schedule'), max_length=6, choices=WORKING_SCHEDULE, default='UND')
    #TODO find a solution for TextField length
    working_task = models.TextField(_(u'Working Task'))
    comment = models.TextField(_(u'Comment'))

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def long_str(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s' % (self.first_name,
                                self.last_name,
                                self.street,
                                self.mobile_number,
                                self.phone_number,
                                self.mail,
                                self.working_place,
                                self.get_working_contract_display(),
                                self.get_working_schedule_display(),
                                self.working_task,
                                self.comment, )
    #TODO an employee need to be unique


class Row(models.Model):
    emp_abs = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_(u'Absent Employee'),
        related_name="emp_abs",
    )
    emp_rep = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_(u'Replacement Employee'),
        related_name="emp_rep",
    )
    date_from = models.DateTimeField(_(u'Date from'))
    date_to = models.DateTimeField(_(u'Date to'))
    absence_reason = models.CharField(_(u'Absence Reason'), max_length=200)

    #TODO overwrite save method
    """"
    Need to check :
    - Row is invalid
    - Emp abs is already absent at this interval
    - Emp abs is already replacement at this interval
    - Emp rep is already absent at this interval
    - Emp rep is already replacement at this interval
    - Row already exists
    """""
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.emp_abs, self.emp_rep, DateFormat(self.date_from).format('j/m/Y H:i:s'), DateFormat(self.date_to).format('j/m/Y H:i:s'), self.absence_reason)