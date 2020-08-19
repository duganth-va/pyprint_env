#!/bin/sh

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

# You can put other setup logic here
exec /usr/bin/ssm-parent --plain-path "/td/envvars/lab/" run -- env LOG_LOCATION=console "$@"
# Evaluating passed command:
#exec "$@"
