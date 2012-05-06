#!/bin/sh

cat names.txt | tr -s ',' '\n' | tr -d \042 | sort > ordenados.txt