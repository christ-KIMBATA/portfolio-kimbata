from django.db import models
from django.utils.text import slugify
class Project(models.Model):
 title=models.CharField(max_length=180)
 slug=models.SlugField(unique=True,blank=True)
 category=models.CharField(max_length=90,default='Infrastructure')
 summary=models.TextField()
 technologies=models.CharField(max_length=255,help_text='Séparer les technologies par des virgules')
 context=models.TextField(blank=True,help_text='Contexte et objectifs spécifiques du projet')
 architecture=models.TextField(blank=True,help_text='Architecture technique et environnement')
 implementation=models.TextField(blank=True,help_text='Mise en œuvre et configuration')
 results=models.TextField(blank=True,help_text='Résultats et bénéfices')
 github_url=models.URLField(blank=True)
 demo_url=models.URLField(blank=True)
 featured=models.BooleanField(default=True)
 order=models.PositiveIntegerField(default=0)
 class Meta:
  ordering=['order','title']
 def save(self,*args,**kwargs):
  if not self.slug:
   self.slug=slugify(self.title)
  super().save(*args,**kwargs)
 def __str__(self):return self.title
 @property
 def tech_list(self):return [x.strip() for x in self.technologies.split(',') if x.strip()]
