from django.db import models
    
class LatestAction(models.Model):
    bill = models.OneToOneField('Bill', on_delete=models.CASCADE, related_name='latest_action_id')
    action_date = models.DateField()
    text = models.CharField(max_length=255)

class Bill(models.Model):
    congress = models.IntegerField()
    # latest_action = models.OneToOneField(LatestAction, on_delete=models.CASCADE, related_name='bill_id') # changed this
    number = models.CharField(max_length=20)
    origin_chamber = models.CharField(max_length=50)
    origin_chamber_code = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=10)
    update_date = models.DateField()
    update_date_including_text = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.title
    
