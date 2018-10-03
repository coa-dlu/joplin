#!/usr/bin/env bash
echo "-- Entrypoint Executed (docker-entrypoint-prod.sh)"
echo "--    HEROKU_APP_NAME:            ${HEROKU_APP_NAME}"
echo "--    HEROKU_SLUG_COMMIT:         ${HEROKU_SLUG_COMMIT}"
echo "--    HEROKU_RELEASE_CREATED_AT:  ${HEROKU_RELEASE_CREATED_AT}"
echo "--    "
echo "--    Bucket: ${AWS_S3_BUCKET}"
echo "--    Bucket User: ${AWS_S3_USER}"
echo "--    Bucket ID: ${AWS_S3_KEYID}"
exec "$@"

