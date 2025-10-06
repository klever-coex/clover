#! /usr/bin/env bash

set -ex # exit on error, echo commands

SCRIPT=$(readlink -f "$0")
REPO_DIR=$(dirname $(dirname "$SCRIPT"))

MAGIC_SCRIPT="sudo /root/init_rpi.sh; sudo sed -i '/sudo \\\/root\\\/init_rpi.sh/d' /etc/rc.local && sudo reboot"
sed -i "19a${MAGIC_SCRIPT}" /etc/rc.local

cp ${REPO_DIR}'/builder/assets/init_rpi.sh' '/root/'
cp ${REPO_DIR}'/builder/assets/hardware_setup.sh' '/root/'

cp ${REPO_DIR}'/clover/udev/99-px4fmu.rules' '/etc/udev/rules.d/'
cp ${REPO_DIR}'/clover/udev/99-thermal-camera.rules' '/etc/udev/rules.d/'

cp ${REPO_DIR}'builder/assets/display.service' '/lib/systemd/system/'

systemctl enable --now display.service

history -c && exit