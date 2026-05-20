from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    input_data = models.TextField()

    expected_output = models.TextField()

    difficulty = models.CharField(
        max_length=20,
        default="Easy"
    )

    def __str__(self):
        return self.title


class Submission(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE
    )

    code = models.TextField()

    language = models.CharField(
        max_length=50,
        default="Python"
    )

    result = models.CharField(
        max_length=50
    )

    score = models.IntegerField(
        default=0
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"