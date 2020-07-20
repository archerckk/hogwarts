#!/bin/bash

browser_dict=('firefox' 'chrome')
for browser in ${browser_dict[*]};
do
    echo $browser
    browser=$browser pytest "selenium_grid_demo.py" &
done
exec /bin/bash