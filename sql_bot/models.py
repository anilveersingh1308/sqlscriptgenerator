from django.db import models

# Create your models here.


class QueryLog(models.Model):
    user_input = models.TextField()
    generated_sql = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input
