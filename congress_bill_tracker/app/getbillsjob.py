from django_cron import CronJobBase, Schedule
import requests
from django.utils import timezone
from .models import Bill, LatestAction
from dateutil.parser import isoparse
from dotenv import load_dotenv
import os

load_dotenv()

class GetBillsJob(CronJobBase):
    RUN_EVERY_MINS = 1440 # every 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.getbillsjob'

    def do(self):
        url = 'https://api.congress.gov/v3/bill'
        params = {
            'limit': 250,
            'fromDateTime': '2024-04-08T00:00:00Z',
            'sort': 'updateDate+asc',
            'api_key': os.getenv('CONGRESS_GOV_API_KEY')
        }
        headers = {
            'accept': 'application/json'
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            bills = data.get('bills', [])

            for bill_data in bills:
                congress = bill_data.get('congress')
                number = bill_data.get('number')
                origin_chamber = bill_data.get('originChamber')
                origin_chamber_code = bill_data.get('originChamberCode')
                title = bill_data.get('title')
                bill_type = bill_data.get('type')
                update_date = bill_data.get('updateDate')
                update_date_including_text = bill_data.get('updateDateIncludingText')
                if update_date_including_text:
                    update_date_including_text = isoparse(update_date_including_text)
                    #  update_date_including_text = timezone.make_aware(update_date_including_text)
                else:
                    update_date_including_text = None
                url = bill_data.get('url')

                # Create or update the Bill
                bill = Bill.objects.create(
                    congress=congress,
                    number=number,
                    origin_chamber=origin_chamber,
                    origin_chamber_code=origin_chamber_code,
                    title=title,
                    bill_type=bill_type,
                    update_date=update_date,
                    update_date_including_text=update_date_including_text,
                    url=url,
                )

                latest_action_data = bill_data.get('latestAction')
                if latest_action_data:
                    action_date = latest_action_data.get('actionDate')
                    action_text = latest_action_data.get('text')

                    # Create or update the LatestAction associated with the Bill
                    latest_action = LatestAction.objects.create(
                        bill=bill,
                        action_date=action_date,
                        text=action_text
                    )

            print('Bills saved successfully.')
        else:
            print(f'Request failed with status code: {response.status_code}')