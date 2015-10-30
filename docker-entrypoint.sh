#!/bin/bash
set -e

if [ "$1" = 'start-ofbiz' ]; then
    PATH_OFBIZ=/data/coclab-ofbiz
    PATH_CONFIG=/data/config

    ##################### handle SIGTERM #####################
    function _term() {
        printf "%s\n" "Caught terminate signal!"
        ${PATH_OFBIZ}/ant stop

        # kill -SIGTERM $child 2>/dev/null
        exit 0
    }

    trap _term SIGHUP SIGINT SIGTERM SIGQUIT

    ##################### generate config #####################
    # List configure files:
    # 1. build.xml: config max memory for jvm ofbiz
    # 2. entityengine.xml
    # 3. url.properties             -> use http only
    #
    # -------------------------------------
    # 1. build.xml
    # 2. framework/entity/config/entityengine.xml
    # 3. framework/webapp/config/url.properties
    # port.https.enabled=Y      ->      N
    #

    # generate file config
    python3 ${PATH_CONFIG}/tmpl/generate_ofbiz_config.py

    # config ofbiz
    cp ${PATH_CONFIG}/tmpl/build.xml ${PATH_OFBIZ}/build.xml
    cp ${PATH_CONFIG}/tmpl/entityengine.xml ${PATH_OFBIZ}/framework/entity/config/entityengine.xml
    cp ${PATH_CONFIG}/url.properties ${PATH_OFBIZ}/framework/webapp/config/url.properties

    ##################### start application #####################
    # start ofbiz
    ${PATH_OFBIZ}/ant start-batch

    # make sure log file existed
    touch ${PATH_OFBIZ}/runtime/logs/ofbiz.log

    tail -f ${PATH_OFBIZ}/runtime/logs/ofbiz.log &
    child=$!
    wait "$child"
fi

exec "$@"
