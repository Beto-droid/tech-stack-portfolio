from django.db import models

class CVEntry(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Blank if it's the current position

    def __str__(self):
        return f"{self.job_title} at {self.company}"