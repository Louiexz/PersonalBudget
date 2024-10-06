from .models import *

class PersonalBudget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    budget = models.CharField(max_length=20, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    validity = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ("Expired", "Expired"),
        ("Not Expired", "Not Expired")
    ])
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')

    def clean(self):
        if self.validity < dates.today():
            self.status = "Expired"
        else:
            self.status = "Not Expired"

    def update_budget(self):
        total_spent = self.transactions.aggregate(total_spent=Sum("price"))["total_spent"] or 0
        self.total_spent = total_spent
        self.remaining_amount = self.total_amount - self.total_spent

    def save(self, *args, **kwargs):
        self.clean()
        self.update_budget()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Budget '{self.budget}': Total {self.total_amount}, Remaining {self.remaining_amount}, Validity {self.validity}."
