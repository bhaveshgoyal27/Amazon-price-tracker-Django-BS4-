from django.db import models
from .utils import get_link_data
# Create your models here.
class Link(models.Model):
	name = models.CharField(max_length=200, blank=True)
	url = models.URLField()
	img_url = models.URLField(blank=True)
	current_price = models.FloatField(blank=True)
	old_price = models.FloatField(default=0)
	price_difference = models.FloatField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('price_difference','-created')

	def save(self, *args,**kwargs):
		name, price, img_url = get_link_data(self.url)
		old_price = self.current_price
		if self.current_price:
			if price!=old_price:
				self.price_difference = round(price-old_price,2)
				self.old_price = old_price
		else:
			self.old_price = price
			self.price_difference = 0
		if not self.img_url:
			self.img_url = img_url
		self.current_price = price
		self.name = name
		super().save(*args,**kwargs)