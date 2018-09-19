#!/usr/bin/env bash


TRAVIS_CI_TEST_TAG="travis-ci-internal-test"

#
# Turn the branch name into the app name in Heroku
# $1 (string) The name of the branch (ie. "staging", "production", "pr-160")
#

function heroku_resolve_appname {
    # Turn the branch name into the application name we need
    # production: joplin
    # staging: joplin-staging
    # anyother: anyother
    case $1 in
        staging)
            APPNAME="joplin-staging"
            ;;
        production)
            APPNAME="joplin"
            ;;
        sergiotest)
            APPNAME="joplin-personal"
            ;;
        *)
            APPNAME=$1
            ;;
    esac

    # Output results for logging
    echo "${APPNAME}"
}

#
# Calls the release function for a specific image to a specific application
# $1 (string) The name of the branch (ie. "staging", "production", "pr-160")
# Example: $ heroku_release staging
#

function heroku_release {

    # Show message if this is an internal test
    if [ "$1" = "travis-ci-internal-test" ]; then
        echo "heroku_release(): Ready to execute.";
        return 0
    fi;

    # Output error if no branch is specified.
    if [ "$1" = "" ]; then
        echo "heroku_release(): Branch name required (ie: '$ heroku_release staging'). Returning Error."
        exit 1
    fi;

    # Retrieve App Name
    APPNAME=$(heroku_resolve_appname $1);

    # Output results for logging
    echo "heroku_release() Branch Name: ${TRAVIS_BRANCH}"
    echo "heroku_release() App name: ${APPNAME}"

    # Determine image id to push
    DOCKER_IMAGE_ID=$(docker inspect registry.heroku.com/$1/web --format={{.Id}})

    # Gemerate json payload to upload via API
    JSON_PAYLOAD='{"updates":[{"type":"web","docker_image":"'"${DOCKER_IMAGE_ID}"'"}]}'

    # Make 'Release' API Call
    curl -n -X PATCH https://api.heroku.com/apps/$1/formation \
    -d "${JSON_PAYLOAD}" \
    -H "Content-Type: application/json" \
    -H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
    -H "Authorization: Bearer ${HEROKU_API_KEY}"

}

#
# retrieve_latest_django_mid - Searches the jopling migrations directory
# and gets the file name of the latest migration id.
#

function retrieve_latest_django_mid {
    # Get a list of all files, orders by ascending numeric order of column 1, 3, 4 (using underscore as separator)
    echo "retrieve_latest_django_mid() Testing retrieve_latest_django_mid";

    echo $TRAVIS_BUILD_DIR/joplin/base/migrations;
    ls $TRAVIS_BUILD_DIR/joplin/base/migrations;
    ls $TRAVIS_BUILD_DIR/joplin/base/migrations | sort -n -t _ -k 1 -k 3 -k 4 | tail -1;
    echo "retrieve_latest_django_mid() Done testing, running script.";

    FILENAME=$(ls $TRAVIS_BUILD_DIR/joplin/base/migrations | sort -n -t _ -k 1 -k 3 -k 4 | tail -1)
    DJMID=$(echo -n $FILENAME | cut -d "." -f 1)

    echo "retrieve_latest_django_mid() Result:"
    echo $DJMID
}

#
# Creates a database backup of a running heroku app (as long as it as a PostgreSQL db attached to it)
#
# $1 (string) The name of the application (ie. "staging", "production")
# Example: $ backup_sql staging
#

function heroku_backup_database {

    # Show message if this is an internal test
    if [ "$1" = "travis-ci-internal-test" ]; then
        echo "heroku_backup_database(): Ready to execute.";
        return 0
    fi;

    # Output error if no branch is specified.
    if [ "$1" = "" ]; then
        echo "heroku_backup_database(): Branch name required (ie: '$ heroku_backup_database staging'). Returning Error."
        exit 1;
    fi;

    # Retrieve App Name
    APPNAME=$(heroku_resolve_appname $1);

    # Output results for logging
    echo "heroku_backup_database() Branch Name: ${TRAVIS_BRANCH}"
    echo "heroku_backup_database() App name: ${APPNAME}"

    # Gather connection string from heroku api
    CONNECTION_STRING=$(heroku config:get DATABASE_URL -a $1);
    DB_NAME=$(echo -n $CONNECTION_STRING | cut -d "/" -f 4);
    DB_TIMESTAMP=$(date '+%Y-%m-%d--%H-%M-%S');

    echo "heroku_backup_database() ----- Performing Database Backup";
    echo "heroku_backup_database() -- Date Timestamp: ${DB_TIMESTAMP}";
    echo "heroku_backup_database() -- DB Name: ${DB_NAME}";
    echo "heroku_backup_database() -- Performing copy, please wait...";

    pg_dump $CONNECTION_STRING | gzip | aws s3 cp - s3://$AWS_BUCKET_BACKUPS/backups/database/$TRAVIS_BRANCH/$1.$DB_TIMESTAMP.$TRAVIS_COMMIT.$.psql.gz;
    echo "heroku_backup_database()----- Finished Performing Database Backup";
}


#
# Creates a database backup of a running heroku app (as long as it as a PostgreSQL db attached to it)
#
# $1 (string) The name of the branch (ie. "joplin-staging", "joplin-personal")
# Example: $ backup_sql staging
#

function backup_psql {

    # Show message if this is an internal test
    if [ "$1" = "travis-ci-internal-test" ]; then
        echo "backup_psql(): Ready to execute.";
        return 0
    fi;

    # Output error if no branch is specified.
    if [ "$1" = "" ]; then
        echo "backup_psql(): Branch name required (ie: '$ backup_psql staging'). Returning Error."
        exit 1;
    fi;

    # Retrieve App Name
    APPNAME=$(heroku_resolve_appname $1);

    # Output results for logging
    echo "backup_psql() Branch Name: ${TRAVIS_BRANCH}"
    echo "backup_psql() App name: ${APPNAME}"

    # Gather connection string from heroku api
    CONNECTION_STRING=$(heroku config:get DATABASE_URL -a $1);
    DB_NAME=$(echo -n $CONNECTION_STRING | cut -d "/" -f 4);
    DB_TIMESTAMP=$(date '+%Y-%m-%d--%H-%M-%S');

    echo "backup_psql() ----- Performing Database Backup";
    echo "backup_psql() -- Date Timestamp: ${DB_TIMESTAMP}";
    echo "backup_psql() -- DB Name: ${DB_NAME}";
    echo "backup_psql() -- Performing copy, please wait...";

    pg_dump $CONNECTION_STRING | gzip | aws s3 cp - s3://$AWS_BUCKET_BACKUPS/backups/database/$TRAVIS_BRANCH/$1.$DB_TIMESTAMP.$TRAVIS_COMMIT.$.psql.gz;
    echo "backup_psql()----- Finished Performing Database Backup";
}




#
# Creates a database backup of a running heroku app (as long as it as a PostgreSQL db attached to it)
#
# $1 (string) The name of the branch (ie. "joplin-staging", "joplin-personal")
# Example: $ backup_sql joplin-personal
#

function heroku_build {

    # Show message if this is an internal test
    if [ "$1" = "travis-ci-internal-test" ]; then
        echo "heroku_build(): Ready to execute.";
        return 0
    fi;

    # Output error if no branch is specified.
    if [ "$1" = "" ]; then
        echo "heroku_build(): Branch name required (ie: '$ backup_psql staging'). Returning Error."
        exit 1;
    fi;

    # Retrieve App Name
    APPNAME=$(heroku_resolve_appname $1);

    # Output results for logging
    echo "heroku_build() Branch Name: ${TRAVIS_BRANCH}"
    echo "heroku_build() App name: ${APPNAME}"

    # Gather connection string from heroku api
    CONNECTION_STRING=$(heroku config:get DATABASE_URL -a $1);
    DB_NAME=$(echo -n $CONNECTION_STRING | cut -d "/" -f 4);
    DB_TIMESTAMP=$(date '+%Y-%m-%d--%H-%M-%S');

    echo "heroku_build() ----- Building Docker Container";
    echo "heroku_build() -- Logging in to Services";
    docker login --username=_ --password=$HEROKU_API_KEY registry.heroku.com
    echo "heroku_build() -- Building";
    docker build -t $JOPLIN_IMAGE_NAME .
    echo "heroku_build() -- Tagging Image";
    docker tag $JOPLIN_IMAGE_NAME registry.heroku.com/$JOPLIN_TARGET/web
    echo "heroku_build() -- Pushing to Heroku Repository";
    docker push registry.heroku.com/$JOPLIN_TARGET/web
    echo "heroku_build()----- Finished Performing Database Backup";
}


#
# helper_test - Tests the helper has been initialized properly and ready to run
# Runs the functions without parameters forcing error output.
#

function helper_test {
    echo "helper_test() ----- Heroku Helper Test Initialized"
    echo "helper_test() ----- Test tag: #{TRAVIS_CI_TEST_TAG}";

    echo "helper_test() ----- Testing 'heroku_release' is ready: ";
    heroku_release "travis-ci-internal-test";

    echo "helper_test() ----- Testing 'backup_psql' is ready: ";
    heroku_backup_database "travis-ci-internal-test";

    echo "helper_test() ----- Testing django migration id: ";
    retrieve_latest_django_mid;

    echo "heroku_build() ----- Testing function is ready: ";
    heroku_build "travis-ci-internal-test";

    echo "helper_test() ----- Heroku Helper Test finished.";
}

