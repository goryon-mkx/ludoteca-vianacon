import pandas as pd
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from backend.api.models import Quota

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file")

    def add_user(self, email, name):
        pass

    def handle(self, *args, **options):
        self.stdout.write(options["file"])
        table = pd.read_csv(options["file"], header=0, delimiter=";")
        for _, row in table.iterrows():

            names = row["Nome"].split(" ")
            email = row["E-mail"]

            group = Group.objects.get(name='Associate')

            user_count = User.objects.filter(email=email).count()
            if user_count == 0:
                user = User(email=email, username=email, first_name=names[0])
                if len(names) > 1:
                    user.last_name = " ".join(names[1:])
                user.save()
            else:
                user = User.objects.get(email=email)

            quotas = row["Quotas"].split(",")

            for year in quotas:
                if Quota.objects.filter(year=year, user=user).count() == 0:
                    q = Quota()
                    q.user = user
                    q.year = year
                    q.save()

            group.user_set.add(user)
            group.save()

