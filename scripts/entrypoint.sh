#!/bin/bash

cd /opt

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --start-service)
    START_SERVICE=true
    shift # past argument
    ;;
    --hot-reload)
    HOT_RELOAD=true
    shift # past argument
    ;;
    *)
    shift # past unknown
    ;;
esac
done


# Start service
if [ "$START_SERVICE" = true ] || [ "$HOT_RELOAD" = true ]
then
    if [ "$HOT_RELOAD" = true ]
    then
      echo "Starting Gunicorn with hot reloading."
      exec gunicorn census.app:app \
          -c /etc/census/conf.py --reload
    else
      echo "Starting Gunicorn."
      exec gunicorn census.app:app \
          -c /etc/census/conf.py
    fi
else
  echo "Not starting service."
fi
                                                                                                                  