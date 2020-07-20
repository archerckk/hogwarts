#!/usr/bin/env bash
devices=`adb devices |grep -w device |awk '{print $1}'`

for device in $devices;do
    echo $device
    udid=$device pytest "test_wework.py" &
done
exec /bin/bash