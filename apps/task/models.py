from config.utils.models import BaseModel
from django.db.models import CharField, ForeignKey, PROTECT, DateField, TextField
from apps.users.models import User
from apps.projects.models import Project

class Task(BaseModel):
    task_creator = ForeignKey(User, on_delete=PROTECT, related_name='task_Creator')
    assigned = ForeignKey(User, on_delete=PROTECT, related_name='assigned')
    project = ForeignKey(Project, on_delete=PROTECT, related_name="task")
    name = CharField(max_length=50, unique=True)
    description = TextField(max_length=300)
    date_start = DateField()
    date_end = DateField()

    class Meta:
        db_table = 'Task'

    def __str__(self):
        return self.name