#!/bin/bash

browser_dict=('edge' 'chrome' )
for browser in ${browser_dict[*]};
do
    echo $browser
    browser=$browser pytest "selenium_grid_demo.py" &
done
exec /bin/bash