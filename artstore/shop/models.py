from django.db import models
from authentication.models import User
from galery.models import Art


class Basket(models.Model):
    art_id = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='basket_art')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket_user')
    prise = models.DecimalField('Стоймость', max_digits=19, decimal_places=2)

    def __str__(self):
        return f"{self.art_id.title}"
