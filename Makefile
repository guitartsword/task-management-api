recreate_db:
	docker compose run --rm -e DROP_ALL=1 fastapi python migrate.py

migrate:
	docker compose run --rm fastapi python migrate.py

seed_db:
	docker compose run --rm -e SEED_DB=1 fastapi python migrate.py

bash:
	docker compose exec fastapi bash
