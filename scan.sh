#!/bin/bash
GRABDIR=`mktemp --tmpdir=. --directory  session_XXX`

for i in {0..10}
do
  mkdir -p grab
  echo "   Turn on lights, then hit ENTER when ready to acquire bg and color images."
  read -p "   You will need to hit ENTER to grab each image and then ESCAPE when finished with color images."
  python color.py
  read -p "   Turn off lights, Hit ENTER when ready to start the scan"
  python acquire.py gray10/*
  mv grab $GRABDIR/grab_$i
  echo "If you're done, type \"quit\" and hit ENTER,"
  echo "  otherwise hit ENTER to acquire another scan from a different viewpoint."
  read -r input
  echo ""
  if [ "$input" = "quit" ]; then
    break
  fi
  printf "\n"
done


