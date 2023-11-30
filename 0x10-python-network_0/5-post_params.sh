#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always he here for PLD " "$1"
