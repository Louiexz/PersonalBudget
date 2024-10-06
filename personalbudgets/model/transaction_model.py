from .models import *

from .budget_model import PersonalBudget
from .category_model import Category

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    validity = models.DateField()
    remaining_installment = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[
        ("Paid", "Paid"),
        ("To Pay", "To Pay")]
    )
    notes = models.TextField(blank=True)
    budget = models.ForeignKey(PersonalBudget, related_name="transactions", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="transactions", on_delete=models.CASCADE)

    def clean(self):
        if self.validity < dates.today():
            raise ValidationError("Validity date cannot be in the past.")
        if self.price < 0:
            raise ValidationError("Transaction price cannot be negative.")
        if self.remaining_installment < 0:
            raise ValidationError("Remaining installments must be positive.")

    def save(self, *args, **kwargs):
        self.clean()
        if self.budget.remaining_amount < self.price:
            raise ValidationError("Transaction price exceeds remaining budget.")
        if self.budget.status != "Expired":
            super().save(*args, **kwargs)
            self.budget.update_budget()
        else:
            raise ValidationError("Expired budget.")

    def __str__(self):
        return f"Transaction '{self.item}': Price {self.price}, Status {self.status}, Validity {self.validity}."

@receiver(post_save, sender=Transaction)
def update_budget_on_transaction_save(sender, instance, **kwargs):
    instance.budget.update_budget()

@receiver(post_delete, sender=Transaction)
def update_budget_on_transaction_delete(sender, instance, **kwargs):
    instance.budget.update_budget()