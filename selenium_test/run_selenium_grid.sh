#!/bin/bash

browser_dict=( 'chrome' )
for browser in ${browser_dict[*]};
do
    echo $browser
    browser=$browser pytest "selenium_grid_demo.py" &
done
exec /bin/bash