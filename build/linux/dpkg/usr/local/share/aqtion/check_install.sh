#!/bin/bash

## Define directories and check for basic commands

COMMAND=$1
AQTION_DIR=${HOME}/aqtion
DISTRIB_URL="https://api.github.com/repos/actionquake/distrib/releases/latest"
ARCH=$(uname -m)

## Check if current context is root, do not install if root
CURRENT_USER=$(whoami)
if [[ ${CURRENT_USER} = "root" ]]
then
    echo "Error: User running script is root, do not install as root"
    exit 1
fi

## This script uses curl, check
if command -v curl &> /dev/null
then
    :
else
    echo "curl not found, please install curl"
    echo "Run this and retry:"
    echo "sudo apt-get update && sudo apt-get install curl -y"
    exit 1
fi

## This script uses unzip, check
if command -v unzip &> /dev/null
then
    :
else
    echo "unzip not found, please install unzip"
    echo "Run this and retry:"
    echo "sudo apt-get update && sudo apt-get install unzip -y"
    exit 1
fi

## Functions
check_for_install () {
    INSTALLED_VERSION=$(grep -s installed_version ${AQTION_DIR}/versions | cut -f 2 -d "=")
    LATEST_VERSION=$(curl -s ${DISTRIB_URL} | grep browser_download_url | cut -d '"' -f 4 | grep client | head -n 1 | cut -d "/" -f 8)

    if [[ ! -f "${AQTION_DIR}/versions" ]]  ## Version not found, assuming this is a fresh install
    then
        download_aqtion
    else
        echo "Existing installation found!"
        echo "If you wish to upgrade to a newer version if one is available, re-run like so: 'aqtion update'"
        launch_game
    fi
}

check_for_updates () {
    if [[ "${INSTALLED_VERSION}" = "${LATEST_VERSION}" ]]
    then
        echo "Installed version is up-to-date, continuing..."
        launch_game
    else
        if [[ -f ${AQTION_DIR}/update_check ]]
        then
            echo "Update check disabled, launching game..."
            launch_game;
        else
            echo "Installed version detected: ${INSTALLED_VERSION}"
            echo "Latest version detected:  ${LATEST_VERSION}"
            read -p "There's a new version of AQtion available, do you want to download it?  (Y)es/(N)o/(D)on't Ask Again:  " ynd
            case $ynd in
                [Yy]* ) download_aqtion;;
                [Nn]* ) launch_game;;
                [Dd]* ) touch "${AQTION_DIR}/update_check"; launch_game;;
                * ) echo "Please answer Y, N or D.";;
            esac
        fi
    fi
}

update_version_number () {
    if [[ -s "${AQTION_DIR}/versions" ]] || [[ ! -f "${AQTION_DIR}/versions" ]]
    then  # Version file not found
        echo "installed_version=${LATEST_VERSION}" >> ${AQTION_DIR}/versions
    else  # Update version
        awk -F '[= ]+' -v name="installed_version" -v value="${LATEST_VERSION}" '$1==name{$2=value}1' ${AQTION_DIR}/version
    fi

}

download_aqtion () {
    mkdir -p ${AQTION_DIR}

    if [[ ${ARCH} = "x86_64" ]]
    then
        LINUX_ARCH="x86_64"
    elif [[ ${ARCH} = "aarch64" ]]
    then
        LINUX_ARCH="arm64"
    else
        echo "x86_64 or aarch64 not detected, please post a Github Issue at https://github.com/actionquake/distrib with the following information:"
        echo "uname: $(uname)"
        echo "arch detected: $(uname -m)"
        return 1
    fi

    ## Zipfile name "aqtion-VERSION-linux-ARCH.zip"

    LATEST_VERSION=$(curl -q -s ${DISTRIB_URL} | grep browser_download_url | cut -d '"' -f 4 | grep ${LINUX_ARCH} | grep -v deb | head -n 1 | cut -d "/" -f 8)
    LATEST_PACKAGE="aqtion-${LATEST_VERSION}-linux-${LINUX_ARCH}.zip"
    echo "Downloading AQtion ${LATEST_VERSION} ..."
    curl --progress-bar -q -s -L -o /tmp/aqtion_${LATEST_VERSION}.zip "https://github.com/actionquake/distrib/releases/download/${LATEST_VERSION}/${LATEST_PACKAGE}"
    extractzip=$(unzip /tmp/aqtion_${LATEST_VERSION}.zip -d "${HOME}")
    if [[ $? = "0" ]]
    then
        update_version_number ${LATEST_VERSION}
        echo "Installation successful!"
        launch_game
    else
        if [[ -z "${LATEST_VERSION}" ]] || [[ -z "${LATEST_PACKAGE}" ]]
        then
            LATEST_VERSION="undefined"
            LATEST_PACKAGE="undefined"
        fi
        echo "Installation failure, take this debug information and post a Github Issue at https://github.com/actionquake/distrib with the following information: "
        echo "Latest version available: ${LATEST_VERSION}"
        echo "Attempted package download: ${LATEST_PACKAGE}"
    fi
}

uninstall () {
    echo "Completely removing AQtion from ${AQTION_DIR} ..."
    removedeb=$(sudo dpkg -r aqtion && sudo dpkg --purge aqtion)
    echo "Debian package successfully removed, deleting local AQtion content..."
    removeaqtion=$(sudo rm -rf ${AQTION_DIR})
    echo "AQtion file removal successful."
    echo "Uninstallation complete."
}

launch_game () {
    cd ${AQTION_DIR} || return
    ${AQTION_DIR}/q2pro
}

# Let's-a go
if [[ ${COMMAND} = "clean" ]]
then
    rm -rf ${AQTION_DIR}/aqtion/versions
    rm -rf ${AQTION_DIR}/update_check
    echo "AQtion directory cleaned and ready to check for updates"
    exit 0
fi

if [[ ${COMMAND} = "update" ]]
then
    if [[ ! -f "${AQTION_DIR}/versions" ]]
    then
        echo "No local install found, downloading the latest version..."
    else
        INSTALLED_VERSION=$(grep -s installed_version ${AQTION_DIR}/versions | cut -f 2 -d "=")
        check_for_updates ${INSTALLED_VERSION}
    fi
fi

if [[ ${COMMAND} = "uninstall" ]]
then
    uninstall
    exit 0
fi

## If no arguments, let's play!
check_for_install