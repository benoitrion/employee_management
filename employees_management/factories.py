import datetime
from django.utils import timezone
import factory
from factory.fuzzy import FuzzyDateTime

from employees_management.models import Employee, Row


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
        django_get_or_create = ('first_name', 'last_name',)

    first_name = factory.Sequence(lambda n: 'firstname%d' %n)
    last_name = factory.Sequence(lambda n: 'lastname%d' %n)


class RowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Row
        django_get_or_create = ('emp_abs', 'emp_rep', 'date_from', 'date_to', 'absence_reason')
        #exclude = ('now',)

    emp_abs = EmployeeFactory()
    emp_rep = EmployeeFactory()
    """
    now = factory.LazyFunction(timezone.datetime.utcnow)
    date_from = factory.LazyFunction(lambda o: o.now - timezone.timedelta(hours=10))
    date_to = factory.LazyFunction(lambda o: o.now + timezone.timedelta(hours=50))
    """
    date_from = FuzzyDateTime(datetime.datetime(2016, 8, 17, tzinfo=timezone.get_current_timezone()), datetime.datetime(2016, 8, 17, tzinfo=timezone.get_current_timezone()))
    date_to = FuzzyDateTime(datetime.datetime(2016, 8, 18, tzinfo=timezone.get_current_timezone()), datetime.datetime(2016, 8, 18, tzinfo=timezone.get_current_timezone()))
    absence_reason = "This is a reason"