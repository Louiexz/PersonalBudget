from .models import *

class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    due_date = models.DateField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ("To Complete", "To Complete"),
        ("Completed", "Completed"),
        ("Not Completed", "Not Completed")
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    def clean(self):
        if self.due_date is None: return
        if self.due_date < dates.today():
            raise ValidationError("Due date cannot be in the past.")
        
        if self.pending_amount >= self.total_amount:
            self.status = "Completed"
    
    def save(self, *args, **kwargs):
        if self.status != "Completed" and self.due_date < dates.today():
            self.status = "Not Completed"
        else:
            self.status = "To Complete"
            self.clean()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Goal '{self.title}': Total {self.total_amount}, Pending {self.pending_amount}, Due date {self.due_date}."
