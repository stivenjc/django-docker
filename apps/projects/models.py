from django.db.models import CharField, ForeignKey, PROTECT, DateField
from apps.users.models import User
from config.utils.models import BaseModel


class Project(BaseModel):
    created_user = ForeignKey(User, on_delete=PROTECT)
    name = CharField(max_length=50, unique=True)
    date_start = DateField()
    date_end = DateField()

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name
