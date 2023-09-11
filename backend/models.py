from django.db import models

# Create your models here.
class Slack(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.CharField(max_length=20)
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=100)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.PositiveIntegerField()

    def __str__(self):
        return self.slack_name