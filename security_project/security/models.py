from django.db import models


class SecurityObject(models.Model):
    CATEGORY_CHOICES = [
        ('special', 'Специальные'),
        ('other', 'Иные'),
        ('public', 'Общедоступные'),
        ('biometric', 'Биометрия'),
    ]
    PEOPLE_CHOICES = [
        ('less_100k', 'Меньше 100 тыс.'),
        ('more_100k', 'Больше 100 тыс.'),
    ]
    THREAT_CHOICES = [
        ('1', 'Тип 1'),
        ('2', 'Тип 2'),
        ('3', 'Тип 3'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    number_of_people = models.CharField(max_length=50, choices=PEOPLE_CHOICES)
    threat_type = models.CharField(max_length=50, choices=THREAT_CHOICES)
    security_level = models.CharField(max_length=50)

    def __str__(self):
        return self.name