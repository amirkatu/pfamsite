from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="امیررضا کریمی")
    title = models.CharField(max_length=100, default="توسعه‌دهنده فول‌استک")
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField(default="متخصص در طراحی و توسعه وب‌سایت‌های مدرن...")
    location = models.CharField(max_length=100, default="تهران، ایران")
    email = models.EmailField(default="amir@example.com")
    phone = models.CharField(max_length=15, default="۰۹۱۲۳۴۵۶۷۸۹")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=80)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech1 = models.CharField(max_length=50, blank=True)
    tech2 = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"