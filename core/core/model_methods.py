def pre_save_uid(uid, sender):
    # Generate UID
    if not uid:
        from core.core.generator import generate_uid
        uid = generate_uid(sender)
    return uid


