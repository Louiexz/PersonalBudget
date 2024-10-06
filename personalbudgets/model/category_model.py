from .models import *

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=20, unique=True)
    notes = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def delete(self, *args, **kwargs):
        self.transactions.all().delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Category '{self.category}': Created_at {self.created_at}, Last update {self.updated_at}."