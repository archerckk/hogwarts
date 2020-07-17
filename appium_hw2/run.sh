#!/bin/bash
devices=`adb devices | grep -w "device" | awk '{print $1}'`
for device in $devices;
do
 { nohup adb -s $device shell monkey -p com.xueqiu.android --pct-touch 30 --pct-nav 40 -v --throttle 100 300 & }
done
