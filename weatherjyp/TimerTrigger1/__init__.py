import datetime
import logging
import json
import time
import sys

import azure.functions as func
from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError

sys.path.append("./")
from . import weather

def main(mytimer: func.TimerRequest, tablePath:func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    tags = weather.naver()
    weather_data = {
            "인천현재온도":tags[0],
            "인천날씨정보":tags[1],
            "부산현재온도":tags[2],
            "부산날씨정보":tags[3],
            "광주현재온도":tags[4],
            "광주날씨정보":tags[5],
            "대전현재온도":tags[6],
            "대전날씨정보":tags[7],
            "대구현재온도":tags[8],
            "대구날씨정보":tags[9],
            "울산현재온도":tags[10],
            "울산날씨정보":tags[11],
            "PartitionKey":"Weather_check",
            "RowKey": time.time()
    }
    print("weather_data=",weather_data)

    tablePath.set(json.dumps(weather_data))