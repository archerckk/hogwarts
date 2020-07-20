@echo off
start java -jar selenium-server-standalone-3.141.59.jar -role hub
start java -jar selenium-server-standalone-3.141.59.jar  -role node -nodeConfig  selenium_node_chrome.json
start java -jar selenium-server-standalone-3.141.59.jar  -role node   -nodeConfig  selenium_node_ie.json
