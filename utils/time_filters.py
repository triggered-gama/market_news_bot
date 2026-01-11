from datetime import datetime, timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")

def is_within_intraday_window(published_at, hours=24):
    """
    Returns True if article is from today (IST)
    or within last N hours.
    """
    if not published_at:
        return False

    now_ist = datetime.now(IST)

    if published_at.tzinfo is None:
        published_at = published_at.replace(tzinfo=pytz.UTC)

    published_ist = published_at.astimezone(IST)

    # Same calendar day
    if published_ist.date() == now_ist.date():
        return True

    # Fallback: last N hours
    if now_ist - published_ist <= timedelta(hours=hours):
        return True

    return False
