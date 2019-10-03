#!/bin/bash

INTERACTIVE=
INPUT_FILE=
CURRENT_DIR=${PWD##*/}
OUTPUT_FILE="${CURRENT_DIR}.html"

usage()
{
    echo "[USAGE] slidegen [[[-f file ] [-i]] | [-h]]"
}

# Show options:
while [ "$1" != "" ]; do
    case $1 in
        -f | --file )           shift
                                INPUT_FILE=$1
                                ;;
        -i | --interactive )    INTERACTIVE=1
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

if [ "$INTERACTIVE" = "1" ]; then
    RESPONSE=
    echo -n "Enter name of output file [$OUTPUT_FILE]: "
    read RESPONSE

    if [ -n "$RESPONSE" ]; then
        OUTPUT_FILE=$RESPONSE
    fi

    if [ -f $OUTPUT_FILE ]; then
        echo -n "Output file exists. Overwrite? [y/n]: "
        read response
        if [ "$RESPONSE" != "y" ]; then
            echo "Exiting program."
            exit 1
        fi
    fi
fi

REPO_ROOT=`git rev-parse --show-toplevel`
SLIDES_ROOT="$REPO_ROOT/Slides"

# Create the static website using reveal-md:
reveal-md $INPUT_FILE --static

# Move the generated index.html page to the Slides directory:
mv "_static/index.html" $SLIDES_ROOT/$OUTPUT_FILE

# Delete the _static directory:
rm -rf "_static/"

# Report success to the user:
echo "[DONE] Slide deck created in $SLIDES_ROOT/$OUTPUT_FILE!"
exit 1
