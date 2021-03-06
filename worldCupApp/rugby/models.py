from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='imgs', blank=True)
    def __unicode__(self):
        return self.user.username
    def profile_picture(self):
    	return self.picture

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']

class Matches(models.Model):
	team1 = models.CharField(max_length=128, unique = True)
	team2 = models.CharField(max_length=128, unique = True)
	team1Score = models.IntegerField(default=0)
	team2Score = models.IntegerField(default=0)

class Coupon(models.Model):
	t1 = models.CharField(max_length=128, unique = True)
	t2 = models.CharField(max_length=128, unique = True)
	t1Pred = models.IntegerField(default=0)
	t2Pred = models.IntegerField(default=0)
	
