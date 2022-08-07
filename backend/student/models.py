from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
import random
from django.utils.deconstruct import deconstructible


def get_email(self):
    return self.email


User.add_to_class("__str__", get_email)


@deconstructible
class ProgramAndBranch(models.Model):
    """
    @Roll_number = B19EE048
    => program = choices
    => name = Electrical Engineering
    => getter = B/EE
    => abbreviation = BTech EE
    => check_cg = to check for branch cg comaprison while listing offers
    """
    CATEGORY = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('Phd', 'Phd'),
        ('Msc', 'Msc'),
        ('MBA', 'MBA')
    )
    program = models.CharField(max_length=10, choices=CATEGORY, default="BTech")
    name = models.CharField(max_length=60, default="Electrical Engineering")
    abbreviation = models.CharField(max_length=20, blank=True, null=True)
    getter = models.CharField(max_length=10, default="B/EE")
    check_gpa = models.BooleanField(default=True)
    usable = models.BooleanField(default=False)

    def __str__(self):
        return self.program + " " + self.name


class StudentProfile(models.Model):
    # Choices
    CATEGORY = (
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    )
    NATION = (
        ('Indian', 'Indian'),
        ('Other', 'Other'),
    )
    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=11)
    year = models.SmallIntegerField()
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True)
    gpa = models.FloatField()
    ug_college = models.TextField(null=True, blank=True, default='')
    ug_gpa = models.FloatField(null=True, blank=True, default=0.0)
    ug_passing_year = models.SmallIntegerField(null=True, blank=True, default=0)
    ug_program_branch = models.TextField(null=True, blank=True, default='')
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    jee_air = models.IntegerField(null=True, blank=True)
    physical_disability = models.BooleanField(default=False)
    nationality = models.CharField(max_length=10, choices=NATION)
    permanent_address = models.TextField()
    current_address = models.TextField()
    x_year = models.SmallIntegerField()
    x_board_name = models.CharField(max_length=100)
    x_percentage = models.CharField(max_length=10)
    xii_year = models.SmallIntegerField()
    xii_board_name = models.CharField(max_length=100)
    xii_percentage = models.CharField(max_length=10)
    banned = models.BooleanField(default=False)
    placed = models.BooleanField(default=False)
    std_image = models.ImageField(default='default.jpg', upload_to='student_images')
    registration_timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #new field
    verified = models.BooleanField(default=False)


    def __str__(self):
        return self.user.get_full_name()


class Resume(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resume')
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=200, null=True, blank=True,
                                 help_text="Enter a reference name for this resume by which you can remember the details of this particular resume")

    def __str__(self):
        if not self.reference:
            return "No reference"
        else:
            return self.reference


def event_pre_save_receiver_student(sender, instance, *args, **kwargs):
    if not instance.roll_no:
        instance.roll_no = instance.user.username


pre_save.connect(event_pre_save_receiver_student, sender=StudentProfile)


def event_pre_save_receiver_resume(sender, instance, *args, **kwargs):
    if (instance.student.user.first_name not in instance.file.name or
            instance.student.user.last_name not in instance.file.name or
            instance.student.roll_no not in instance.file.name or
            'IITJodhpur.pdf' not in instance.file.name) \
            and instance._state.adding is True:
        instance.file.name = instance.student.user.first_name + '_' + instance.student.user.last_name \
            + '_' + instance.student.roll_no + '_' + str(random.randint(1, 10001)) + \
            '_' + 'IITJodhpur.pdf'
    if not instance.reference:
        instance.reference = instance.file.name


pre_save.connect(event_pre_save_receiver_resume, sender=Resume)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()


post_delete.connect(delete_user, sender=StudentProfile)
