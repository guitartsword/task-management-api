import os
from core.db import init_db, seed_db, drop_db

if __name__ == "__main__":
    if os.environ.get('DROP_ALL'):
        drop_db()
        print("Deleted all tables")
    init_db()
    print("Created missing tables")
    if os.environ.get('SEED_DB'):
        seed_db()
        print("Added seed data")
