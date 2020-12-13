import datetime
import logging
import subprocess

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
    
    result = subprocess.run(["./bin/cncli", "ping","--host","north-america.relays-new.cardano-mainnet.iohk.io"],capture_output=True)
    logging.info(result)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)