#!/usr/bin/bash
inotifywait -m -r -c "${WATCH_DIR}"| /path/to/watch.py "${WATCH_CONFIG}"
