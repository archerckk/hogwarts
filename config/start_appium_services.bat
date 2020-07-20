@echo off
start java -jar selenium-server-standalone-3.141.59.jar -role hub
start appium -p 4731 --nodeconfig appium_node1.json --session-override
start appium -p 4733 --nodeconfig appium_node2.json --session-override