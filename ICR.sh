#!/bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib
/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java -Djava.library.path=./lib -jar units/ManualApp.jar ICR=$1

