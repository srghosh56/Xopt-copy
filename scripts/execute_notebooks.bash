#!/bin/bash

# Define an array of SKIP values
SKIP=("parallel" "mobo")

NOTEBOOKS=$(find . -type f -name "*.ipynb" -not -path '*/.*')

echo "$NOTEBOOKS"

# Function to check if a file should be skipped
should_skip() {
    local file="$1"
    for skip_value in "${SKIP[@]}"; do
        if [[ "$file" == *"$skip_value"* ]]; then
            return 0 # Skip
        fi
    done
    return 1 # Don't skip
}

for file in $NOTEBOOKS
do
    if should_skip "$file"; then
        echo "Skipping $file"
        continue
    fi

    echo "Executing $file"
    jupyter nbconvert --to notebook --execute "$file" --inplace
done

