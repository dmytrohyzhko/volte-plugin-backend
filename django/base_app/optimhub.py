import requests
import csv
import time
import re
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .models import *

def fetch_optimhub_advertisers():

    print('fetching')

    try:
        url = "https://api.optimhub.com/api/advertisers"
        headers = {
            "x-api-key": "PRh.Ciq+7Ej1~-.E6P7539O0"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            results = data['results']
            for ads in results:
                ModelOptimHubAds(
                    ads_id=ads['id'],
                    name=ads['name'],
                    website=ads['website'],
                    country=ads['country'],
                    created_at=datetime.now()
                ).save()
            return data
        else:
            raise Exception("Faild to fetch API")
    except Exception as error:
        print(f'Faild to fetch_optimhub_advertisers {error}')
        
def start_optimhub_schedular():
    fetch_optimhub_advertisers()

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_optimhub_advertisers, 'interval', seconds=60 * 60)
    scheduler.start()