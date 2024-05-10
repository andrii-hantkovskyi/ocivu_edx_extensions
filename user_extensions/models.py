from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext as _

User = get_user_model()

class ExtendedUserProfile(models.Model):
    IDENTITY_CHOICES = (
        ("russian_federation", "Российская Федерация"),
        ("belarus", "Беларусь"),
        ("ukraine", "Україна"),
        ("kazakhstan", "Қазақстан"),
        ("adige", "Адыгэ"),
        ("altay", "Алтай"),
        ("bashkorstan", "Башҡортостан"),
        ("buryad_ulas", "Буряад Улас"),
        ("dagestan", "Дагестан"),
        ("ingriya", "Ингрия"),
        ("ingushetia", "Ингушетия / ГӀалгӏайче"),
        ("keberday_balkyer", "Къэбэрдей-Балъкъэр / Къабарты-Малкъар"),
        ("kalmikiya", "Калмыкия / Хальмг Таңһч"),
        ("karachay_cherkes", "Къарачай-Черкес / Къэрэшей-Адыгэ"),
        ("kareliya", "Карелия / Karjala"),
        ("komi", "Коми"),
        ("kuban", "Кубань"),
        ("mariy_el", "Марий Эл"),
        ("mokshen_mastor", "Мокшень Мастор"),
        ("mordoviya", "Мордовия"),
        ("saha", "Саха (Якутия)"),
        ("north_osetia", "Северная Осетия — Алания / Цӕгат Ирыстон — Алани"),
        ("syberia", "Сибирь"),
        ("tatarstan", "Татарстан"),
        ("tiva", "Тыва"),
        ("udmurtiya", "Удмуртия"),
        ("ural", "Урал"),
        ("hakasiya", "Хакасия"),
        ("chechen_republic", "Чеченская Республика / Нохчийн Республика"),
        ("chuvashiya", "Чувашия / Чӑва́ш Республики́"),
        ("erzan_mastor", "Эрзянь Мастор / Ěrzäń Mastor"),
        ("other", "(другое)"),
        ("not_set", "(не хочу указывать)"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extended_user_profile', unique=True)
    identity = models.CharField(choices=IDENTITY_CHOICES, max_length=255, blank=True, null=True, verbose_name=_("Identity"))
