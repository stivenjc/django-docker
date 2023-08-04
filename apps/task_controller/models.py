from config.utils.models import BaseModel
from config.utils.choices import STATE_TASK
from django.db.models import CharField, TextField, DateTimeField, BooleanField, CharField

class TaskController(BaseModel):
    name =CharField(max_length=100)
    description = TextField()
    date_and_time = DateTimeField()
    is_active = BooleanField(default=True)
    state_task = CharField(max_length=100,
        choices=STATE_TASK,
        default=STATE_TASK[0][0],
    )

    def __str__(self):
        return f'{self.name}---{self.state_task}'