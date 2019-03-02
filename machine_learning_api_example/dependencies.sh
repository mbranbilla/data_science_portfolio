#!/bin/sh
# Update the repositories
apk update

# Install dependencies

##  apk add <package>
##  apk add --no-cache --virtual build-dependencies

# Remove the temporary dependencies
apk del build-dependencies