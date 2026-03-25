import random

def get_weather():
    """
    Try to fetch real weather (future).
    Fallback to random if unavailable.
    """

    try:
        # Placeholder for real API call
        # Example later: requests.get(...)
        
        raise Exception("API not implemented")

    except:
        # 🔥 FALLBACK SYSTEM
        return random.choice(["sunny", "rain", "heat", "cold"])
