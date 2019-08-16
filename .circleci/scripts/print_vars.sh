#!/usr/bin/env bash
set -e

function print_var {
  echo "$1: [${!1}]"
}

echo "########"
echo "Here's what's stored in CircleCI:"
echo "########"
print_var "CI_AWS_BUCKET_REVIEWAPPS"
print_var "CI_AWS_S3_BUCKET_ARCHIVE"
print_var "CI_AWS_S3_BUCKET_ARCHIVE_LOCATION"
