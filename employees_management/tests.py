from django.test import TestCase
from datetime import datetime

# Create your tests here.
from django.utils.timezone import is_aware

from employees_management.factories import EmployeeFactory, RowFactory
from employees_management.models import Employee, Row

# Must use '1/07/2005 13:33' format
def str_to_dtime(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y %H:%M')


class EmployeeTest(TestCase):
    def test_create_emp_empty(self):
        pass

    def test_create_short_emp(self):
        first_name = "Benoit"
        last_name = "Rion"
        mail = "benoitrion@gmail.com"
        phone_number = "0474266759"

        employee = EmployeeFactory(first_name=first_name,
                                   last_name=last_name,
                                   mail = mail,
                                   phone_number = phone_number,)
        #print employee
        #print employee.long_str()

        employees_from_db = Employee.objects.all()
        self.assertEquals(len(employees_from_db), 1)
        emp_from_db = employees_from_db[0]
        self.assertEquals(emp_from_db, employee)

        self.assertEquals(emp_from_db.first_name, first_name)
        self.assertEquals(emp_from_db.last_name, last_name)
        self.assertEquals(emp_from_db.mail, mail)
        self.assertEquals(emp_from_db.phone_number, phone_number)

    def test_create_complete_employee(self):

        first_name = "Benoit"
        last_name = "Rion"
        mobile_number = "0474266759"
        phone_number = "063444357"
        mail = "benoitrion@gmail.com"
        working_place = "Tintigny"
        working_contract = "CDD_CDI"
        working_schedule = "UND"
        working_task = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tincidunt ullamcorper."
        comment = "This is a commment"

        employee = EmployeeFactory(first_name=first_name,
                                   last_name=last_name,
                                   mobile_number = mobile_number,
                                   phone_number = phone_number,
                                   mail = mail,
                                   working_place = working_place,
                                   working_contract = working_contract,
                                   working_schedule = working_schedule,
                                   working_task = working_task,
                                   comment = comment,)

        employees_from_db = Employee.objects.all()
        self.assertEquals(len(employees_from_db), 1)
        emp_from_db = employees_from_db[0]
        self.assertEquals(emp_from_db, employee)

        self.assertEquals(emp_from_db.first_name, first_name)
        self.assertEquals(emp_from_db.last_name, last_name)
        self.assertEquals(emp_from_db.mobile_number, mobile_number)
        self.assertEquals(emp_from_db.phone_number, phone_number)
        self.assertEquals(emp_from_db.mail, mail)
        self.assertEquals(emp_from_db.working_place, working_place)
        self.assertEquals(emp_from_db.get_working_contract_display(), "CDD-CDI")
        self.assertEquals(emp_from_db.get_working_schedule_display(), "Undefined")
        self.assertEquals(emp_from_db.working_task, working_task)
        self.assertEquals(emp_from_db.comment, comment)

        # print emp_from_db.long_str()

    def test_edit_employee(self):
        pass

    def test_edit_wrong(self):
        pass

    # TODO inplement delete model method
    def test_delete_employee(self):
        emp_factory_1 = EmployeeFactory()
        emp_factory_2 = EmployeeFactory()

        employees_from_db = Employee.objects.all()
        self.assertEquals(len(employees_from_db), 2)
        self.assertEquals(employees_from_db[0], emp_factory_1)
        self.assertEquals(employees_from_db[1], emp_factory_2)

        #print employees_from_db

        # Delete employee 1
        Employee.objects.filter(first_name=emp_factory_1.first_name).delete()

        employees_from_db = Employee.objects.all()
        self.assertEquals(len(employees_from_db), 1)
        self.assertEquals(employees_from_db[0], emp_factory_2)

        #print employees_from_db

    def test_equals_employees(self):
        pass

    #TODO Should an employee be unique ?

class RowTest(TestCase):

    def test_create_row_factories(self):
        row = RowFactory()

        rows_from_db = Row.objects.all()
        self.assertEquals(len(rows_from_db), 1)

        row_from_db = rows_from_db[0]
        self.assertEquals(row.emp_abs, row_from_db.emp_abs)
        self.assertEquals(row.emp_rep, row_from_db.emp_rep)
        self.assertEquals(row.date_from, row_from_db.date_from)
        self.assertEquals(row.date_to, row_from_db.date_to)
        self.assertEquals(row.absence_reason, row_from_db.absence_reason)

    def test_create_row_ok(self):
        emp1 = EmployeeFactory(first_name="Benoit", last_name="Rion")
        emp2 = EmployeeFactory(first_name="Justine", last_name="Rion")

        #date_from = str_to_dtime('1/07/2005 13:33')
        #date_to = str_to_dtime('4/02/2005 15:00')

        reason = "This is a reason"

        row = RowFactory()

        rows_from_db = Row.objects.all()
        self.assertEquals(len(rows_from_db), 1)

        row_from_db = rows_from_db[0]
        self.assertEquals(row.emp_abs, row_from_db.emp_abs)
        self.assertEquals(row.emp_rep, row_from_db.emp_rep)
        print is_aware(row.date_from)
        print is_aware(row_from_db.date_from)
        self.assertEquals(row.date_from, row_from_db.date_from)
        print is_aware(row.date_to)
        print is_aware(row_from_db.date_to)
        self.assertEquals(row.date_to, row_from_db.date_to)
        self.assertEquals(row.absence_reason, row_from_db.absence_reason)

    # TODO some attributes need to be mandatory (emp1, emp2, date_from, date_to)
    def test_create_row_missing_attributes(self):
        row = RowFactory

        pass

    def test_create_row_invalid_dates(self):
        pass

    def test_same_employee(self):
        emp1 = EmployeeFactory(first_name="Benoit", last_name="Rion")
        row = RowFactory(emp_abs=emp1, emp_rep=emp1, )
        pass

    def test_dateto_before_datefrom(self):
        pass

    def test_row_null(self):
        pass

    def test_emp1_already_absent(self):
        pass

    def test_emp1_already_replacement(self):
        pass

    def test_row_edit_ok(self):
        pass

    def test_row_edit_null_attribute(self):
        pass

    def test_row_edit_dateto_before_datefrom(self):
        pass

    def test_row_delete(self):
        pass

    #TODO implement is_emp_abs and is_emp_rep
    def test_check_is_emp_abs(self):
        pass

    def test_check_is_emp_rep(self):
        pass

    def test_row_equals(self):
        pass

    # Row invalid
    def test_invalid_row(self):
        pass

    # Emp abs is already absent at this interval
    def test_emp_abs_is_already_abs(self):
        pass

    # Emp abs is already replacement at this interval
    def test_emp_abs_is_already_rep(self):
        pass

    # Emp rep is already absent at this interval
    def test_emp_rep_is_already_abs(self):
        pass

    # Emp rep is already replacement at this interval
    def test_emp_rep_is_already_rep(self):
        pass

    # Row already exists
    def test_existing_row(self):
        pass
