#!/bin/bash
hcitool lescan>result.txt &  
sleep 5  
pkill --signal SIGINT hcitool