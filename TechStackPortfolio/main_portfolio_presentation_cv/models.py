from PIL import Image
from django.db import models
from django.db.models import ForeignKey, ManyToManyField
from django.core.exceptions import ValidationError
from django.conf import settings

class JobTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    years_in_company = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current_work = models.BooleanField(default=False)
    work_position = models.CharField(max_length=50, default="")
    technologies = ManyToManyField(Technologies)
    company_logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.years_in_company} years"

class SocialLinkConnect(models.Model):
    social_name = models.CharField(max_length=100)
    url = models.URLField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length=255, blank=True, null=True)

    def clean(self):
        # Custom val: url or mail must be set.
        if not self.url and not self.mail:
            raise ValidationError("Either 'url' or 'mail' must be provided for a social link.")

    def __str__(self):
        return f"{self.social_name} - URL: {self.url or 'None'} - Email: {self.mail or 'None'}"

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url_name_to_app = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technologies)
    project_picture = models.ImageField(upload_to='project_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.technologies}"


class UserData(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    job_title = ForeignKey(JobTitle, on_delete=models.CASCADE)
    work_experience = ManyToManyField(WorkExperience, blank=True)
    technologies = ManyToManyField(Technologies, blank=True)
    social_link_connect = ManyToManyField(SocialLinkConnect, blank=True)
    projects = ManyToManyField(Projects, blank=True)
    about_me = models.TextField(max_length=1000, default='Missing About Me')
    bio_picture = models.ImageField(upload_to='bio_images/', null=True, blank=True)
    hero_image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    logo_picture = models.ImageField(upload_to='logo_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.hero_image:
            img = Image.open(self.hero_image.path)
            if img.height > 1080 or img.width > 1920:
                img = img.resize((1920, 1080), Image.Resampling(1))
                img.save(self.hero_image.path)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)



