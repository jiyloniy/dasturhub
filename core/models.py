from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Leads Model


class Period(models.Model):
    name = models.CharField(max_length=250)
    forPeriod = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def unarchived_leads(self):
        return self.leads_set.filter(archive=False)

    def __str__(self) -> str:
        return self.name


class Leads(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    ledstype = models.ForeignKey(
        Period, on_delete=models.CASCADE, blank=True, null=True)

    status = models.CharField(max_length=100, blank=True, null=True),

    is_cheked = models.BooleanField(default=False)

    archive = models.BooleanField(default=False)

    # monthly leads counter fuction
    @property
    def monthly_leads(self):
        return self.objects.filter(created_at__month=5).count()

    def __str__(self):
        return self.name


class Student(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=50)
    female = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    borthday = models.CharField(max_length=50)
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(
        'Groups', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class WeekDay(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField("Price (UZS)")

    # Use a MultipleChoiceField for days of the week
    DAYS_OF_WEEK_CHOICES = [
        (1, 'Dushanba'),    # Monday
        (2, 'Seshanba'),    # Tuesday
        (3, 'Chorshanba'),  # Wednesday
        (4, 'Payshanba'),   # Thursday
        (5, 'Juma'),        # Friday
        (6, 'Shanba'),      # Saturday
        (7, 'Yakshanba'),   # Sunday
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name='courses')
    day = models.ManyToManyField(WeekDay)

    beginday = models.DateField()
    endday = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sepciality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class for Finance. it has amount of expenses,new expenses and income, new income, total income, total expenses, total profit


class Finance(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            total_income=models.Sum('income__amount'),
            total_expenses=models.Sum('expenses__amount'),
            total_profit=models.Sum('income__amount') -
            models.Sum('expenses__amount'),
            new_income=models.Sum('income__amount'),
            new_expenses=models.Sum('expenses__amount'),
        )


# class for Reports (hisobotlar)

class Reports(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    finance = Finance()

    def __str__(self):
        return self.name
