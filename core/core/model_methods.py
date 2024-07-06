from datetime import datetime

from django.utils import timezone


def pre_save_uid(uid, sender):
    # Generate UID
    if not uid:
        from core.core.generator import generate_uid
        uid = generate_uid(sender)
    return uid


def calculate_score(bought_count, views_count, stock, created):
    # Define weights
    weight_for_purchase = 2
    weight_for_views = 0.1
    weight_for_inventory = 0.5

    # Calculate age factor for products older than 1 month
    age_factor = max(0, (timezone.now() - created).days - 30) * 0.05

    # Calculate score
    score = (
        (bought_count * weight_for_purchase) +
        (views_count * weight_for_views) +
        (stock * weight_for_inventory) +
        age_factor
    ) / 4
    # Normalize score (example normalization, adjust as needed)
    normalizing_factor = 10
    final_score = (score / normalizing_factor)
    print(f'Score: {final_score}')
    return final_score

