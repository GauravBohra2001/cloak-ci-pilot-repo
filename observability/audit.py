import logging

logger = logging.getLogger(__name__)


# FALSE POSITIVE TEST: "password" as a noun in an error status message
# Should NOT fire — our pii_in_logs fix excludes error-context noun phrases
def login_failed(username: str) -> None:
    logger.warning("Login failed — wrong password provided by user %s", username)
    logger.info("Password attempt rejected for account %s", username)


# TRUE POSITIVE: logging an actual email variable value
def registration_failed(nickname: str, email: str) -> None:
    logger.warning('Registration failed for user "%s" with email: %s', nickname, email)
