# dirwatch-replacement

watch.service is a systemd service which sets environment vars WATCH_DIR and WATCH_CONFIG executes watch.sh

watch.sh runs inotifywait and pipes output to watch.py

watch.py parses the lines from inotifywait, and based on the WATCH_CONFIG, performs actions based on regex patterns for new files
