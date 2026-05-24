from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)



class Todo(models.Model):
    class StateChoices(models.TextChoices):
        DONE = 'Done', 'Done'
        NOT_DONE = 'Not done', 'Not done'

    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='todos')
    state = models.BooleanField(
        choices=[
            (True, StateChoices.DONE),
            (False, StateChoices.NOT_DONE)
        ],
        default=False
    )
    is_done = models.BooleanField(default=False)
