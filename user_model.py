#Create django models with User, Address and Remark tables. User can have mutiple addresses and one Remark

class User(models.Model):

    user_name = models.CharField(max_length = 50, blank=True)
    first_name = models.CharField(max_length = 50, blank=True)
    last_name = models.CharField(max_length = 50, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    phone = models.IntegerField(blank=True)

    class Meta:
        unique_together = ['user_name', 'email', 'phone']

class Adress(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    adress = models.CharField(max_length=31, blank=True)

class Remark(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    rematk = models.CharField(max_length=31, blank=True)

    class Meta:
        unique_together = ['user', 'remark']

