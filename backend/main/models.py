from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
import re


class OfficeMails(models.Model):
    CATEGORY = (
        ('Suggestion Recipient', 'Suggestion Recipient'),
        ('Inquiry Recipient', 'Inquiry Recipient'),
        ('Advertisement Recipient', 'Advertisement Recipient'),
        ('CC', 'CC'),
        ('BCC', 'BCC'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Office Mails'


class News(models.Model):
    title = models.CharField(max_length=64, blank=True)
    order_no = models.PositiveSmallIntegerField(default=512)
    content = models.TextField(max_length=512)
    active = models.BooleanField(default=True)
    document = models.FileField(upload_to='news', blank=True, null=True)
    file_title = models.CharField(max_length=64, default='Read More')
    link = models.URLField(blank=True, null=True)
    link_title = models.CharField(max_length=64, default='Link')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


class AboutUs(models.Model):
    title = models.CharField(max_length=64, blank=True, default="About Us")
    content = RichTextUploadingField(blank=True, null=True)
    short_content = RichTextUploadingField(blank=True, null=True, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'About Us'


class DirectorMessage(models.Model):
    title = models.CharField(max_length=64, blank=True, default="Director Message")
    name = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to='people')
    content = RichTextUploadingField(max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Director Message'


class PastRecruiters(models.Model):
    company_order_no = models.PositiveIntegerField(default=64)
    company_name = models.CharField(max_length=64)
    company_logo = models.ImageField(upload_to='company-logo', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'Past Recruiters'


class DesignationChoices(models.Model):
    Team_Member = 'Team Member'
    designation = models.CharField(max_length=64, default=Team_Member)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name_plural = 'Designation Choices'


class CoreTeamContacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.ForeignKey(DesignationChoices, on_delete=models.SET_NULL, null=True, blank=True)
    sub_designation = models.CharField(max_length=64, default='Career Development Cell')
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='contacts', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def get_github_username(self):
        x = re.split("https://github.com/", str(self.github_link))
        return x[1]

    def get_linkedin_username(self):
        x = re.split("https://www.linkedin.com/in/", str(self.linkedin_link))
        return x[1]

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name_plural = 'Core Team Contacts'


class VolunteersYearChoices(models.Model):
    year = models.CharField(max_length=64)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name_plural = 'Volunteers Year Choices'


class Volunteers(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    year = models.ForeignKey(VolunteersYearChoices, on_delete=models.SET_NULL, null=True, blank=True)
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Volunteers'


class AlumniTestimonial(models.Model):
    alumni_name = models.CharField(max_length=64)
    company_working = models.CharField(max_length=64)
    designation = models.CharField(max_length=64, null=True)
    testimonial = models.TextField(max_length=361, null=False)
    readmore = models.TextField(null=True, blank=True)
    alumni_image = models.ImageField(upload_to='alumni-testimonial')
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    mailId = models.EmailField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.alumni_name

    class Meta:
        verbose_name_plural = 'Alumni Testimonial'


class Achievements(models.Model):
    CATEGORY = (
        ('Highlight', 'Highlight'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=10, choices=CATEGORY)
    description = RichTextUploadingField(blank=True, null=True)
    details = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='achievements', blank=True, null=True)
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Achievements'


class CareerDevelopmentActivity(models.Model):
    CATEGORY = (
        ('Upcoming', 'Upcoming'),
        ('Past', 'Past'),
    )
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=10, choices=CATEGORY)
    date = models.CharField(default="Thursday, January 10th", blank=True, null=True, max_length=100)
    time = models.CharField(default="4:00pm-6:00pm", blank=True, null=True, max_length=100)
    location = models.TextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    details = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='CDActivities', blank=True, null=True)
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Career Development Activities"


class HomeImageCarousel(models.Model):
    ordering = models.PositiveIntegerField(default=64)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='homepage-carousel', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Home Image Carousel'


class CareerCommittee(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default='Member')
    email = models.EmailField(max_length=32, blank=False, null=False, default='member@gmail.com')
    designation = models.ForeignKey(DesignationChoices, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.TextField(max_length=64, default="Department")
    profile_image = models.ImageField(upload_to='contacts', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Career Committee'


class NavBarSubOptions(models.Model):
    """
    model for frontend data:
        Internships
        Poster
        Brochure
        Past Recruiters Private
        Past Recruiters Public
        Reach Us
        PlacementStatistics
        AIPC Norms
        StudentGuidelines
        Invitation
        Internship Announcement Form
        Job Announcement Form
        Upcoming Companies
    """
    title = models.CharField(max_length=64)
    description = RichTextUploadingField(blank=True, null=True)
    file = models.FileField(upload_to='files', null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = NavBarSubOptions.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        slug = original_slug
        while queryset:
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = NavBarSubOptions.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug
        super(NavBarSubOptions, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Navbar Sub Options'


class WhyRecruit(models.Model):
    title = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    text = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='whyrecruitimages', blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Why Recruit'


class CourseHighlights(models.Model):
    program = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = RichTextUploadingField()
    brochure = models.FileField(upload_to='department_brochure', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Course Highlights'


class PlacementCalendar(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Placement Calendar'


class SheetsPlacementCalendar(models.Model):
    PLACEMENT_CALENDAR_CHOICES = (
        ('internship', 'Internship'),
        ('placement', 'Placement'),
    )
    type = models.CharField(choices=PLACEMENT_CALENDAR_CHOICES, max_length=20)
    calendar_publish_link = models.URLField(max_length=2000, help_text='Keep only the src link of the published google sheet iframe')
    applicable_years = models.CharField(max_length=100, help_text='Enter the years separated by comma. Ex: B20, M21')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Google Sheets Placement Calendar'
