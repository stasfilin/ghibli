from celery.schedules import crontab
from celery.task import periodic_task

from movies.ghibli import Ghibli
from utils.log import logger


@periodic_task(run_every=(crontab(minute="*/1")), name="sync_data", ignore_result=True)
def sync_data() -> None:
    """
    Celery function for fetching ghibli data every 1 min
    """
    logger.info("Sync Ghibli task - started")
    ghibli = Ghibli()
    ghibli.sync()
    logger.info("Sync Ghibli task - finished")
