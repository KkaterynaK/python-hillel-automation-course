import logging


def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    logger = logging.getLogger("log_event")
    logger.setLevel(logging.INFO)

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
