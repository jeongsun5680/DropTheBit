from djongo import models

class User(models.Model):

    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=20)
    # star_coin = models.ArrayField()
    objects = models.DjongoManager()