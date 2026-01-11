# TODO: Switch Database from MySQL to SQLite

- [ ] Update `interview_system/settings.py` to change DATABASES configuration to use SQLite
- [ ] Update `requirements.txt` to remove `mysqlclient`
- [ ] Run `python manage.py migrate` to create the SQLite database and apply migrations
