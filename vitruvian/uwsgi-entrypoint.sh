#!/usr/bin/env bash
# make sure work dir is the same as file location
# ref: https://stackoverflow.com/questions/3349105/how-to-set-current-working-directory-to-the-directory-of-the-script
cd "${0%/*}"
# run uwsgi
uwsgi --ini uwsgi.ini
