from .models import MyData
from django.db import connections
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        external_conn = connections['external_mysql']

        with external_conn.cursor() as cursor:
            query = 'SELECT * FROM external_table WHERE created_at > %s'
            last_entry = MyData.objects.latest('create_at')

            last_time = last_entry.create_at if last_entry else None

            if last_time:
                cursor.execute(query, (last_time,))
            else:
                cursor.execute('SELECT * FROM external_table')
            
            new_data = cursor.fetchall()

            for row in new_data:
                new_record = MyData(
                    id = row[0],
                    data_field = row[1],
                    created_at = row[2]
                )
                new_record.save()

        self.stdout.write(self.style.SUCCESS('Successfully copied new data to Django DB!!'))