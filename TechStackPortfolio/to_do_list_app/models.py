from django.conf import settings
from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    todo_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} with user {self.todo_user}, is completed {self.is_completed} and was created at {self.created_date}"