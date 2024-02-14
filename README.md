# firebase-auth-admin-app
this is a simple cli app to manage users in firebase authenticator.

## quickstart
```sh
# clone the repo
git clone https://github.com/dokxid/firebase-auth-admin-app.git
cd firebase-auth-admin-app

# setup ur dotenv
cp .env.example .env

# run the app
poetry install
poetry run python app.py
```
will give you
```
$ poetry run python app.py      
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list    list all user objects.
  update  set a field in user object
```
## configuration
follow the instructions listed in `.env`:
```sh
# this is an (.env) example file,
# rename this file (.env.example) to .env

# put in ur secret firebase admin sdk json:
# formatted like this: path/to/serviceAccountKey.json
# for reference: https://firebase.google.com/docs/admin/setup
SECRET_PATH=

# put in ur firebase emulator link
# by default: FIREBASE_AUTH_EMULATOR_HOST="127.0.0.1:9099"
# for reference: https://firebase.google.com/docs/emulator-suite
# if u want to access ur production authentication db instead of your emulator,
# comment this out:
FIREBASE_AUTH_EMULATOR_HOST="127.0.0.1:9099"
```

## relevant links
- [Firebase Ddmin SDK Documentation](https://firebase.google.com/docs/admin/setup)
- [Firebase Emulator Suite Documentation](https://firebase.google.com/docs/emulator-suite)