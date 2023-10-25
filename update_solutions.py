import src.utils.updates

try:
    src.utils.updates.update_database()
except Exception:
    print("Could not update database, skipping.")

src.utils.updates.create_components()
