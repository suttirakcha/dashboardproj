from django.db import models

# Create your models here.

CURRENCY_CHOICE = (
    ('THB', 'THB'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    ('JPY', 'JPY'),
    ('AUD', 'AUD'),
    ('CAD', 'CAD'),
)

ENTRY_CHOICES = (
    ('JE', 'Journal Entry'),
    ('ICJE', 'Inter Company Journal Entry'),
    ('BE', 'Bank Entry'),
    ('CE', 'Cash Entry'),
    ('CCE', 'Credit Card Entry'),
    ('DN', 'Debit Note'),
    ('CN', 'Credit Note'),
    ('COE', 'Contra Entry'),
    ('EE', 'Excise Entry'),
    ('WOE', 'Write Off Entry'),
    ('OE', 'Opening Entry'),
    ('DE', 'Depreciation Entry'),
    ('ERR', 'Exchange Rate Revaluation'),
    ('EGOL', 'Exchange Gain Or Loss'),
    ('DR', 'Deferred Revenue'),
    ('DFE', 'Deferred Expense')
)

class Topbar(models.Model):
    text = models.CharField(max_length=255)
    enable_topbar = models.BooleanField(default=False)

class JournalEntry(models.Model):
    title = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=255,choices=ENTRY_CHOICES,default='JE')
    currency = models.CharField(max_length=255,choices=CURRENCY_CHOICE,default='THB')
    currency_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Journal entries'
        verbose_name = 'Journal entry'
