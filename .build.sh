#!/bin/bash

NAME="Rebalanced Rebalance Redux"

if [ -e "$NAME.zip" ]; then
	rm "$NAME.zip"
fi

"C:\Program Files\7-Zip\7z.exe" a -tzip "$NAME.zip" "*.esp" README.md
