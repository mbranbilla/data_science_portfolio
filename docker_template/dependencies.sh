#!/bin/sh
# Update the repositories
apk update

# Install dependencies
apk add --no-cache --virtual build-dependencies gcc python3-dev musl-dev
apk add postgresql-dev make

# Remove the temporary dependencies
apk del build-dependencies