#!/bin/bash

input_folder="./picture"
output_folder="./compressed_images"

mkdir -p "$output_folder"

find "$input_folder" -type f \( -iname \*.jpg -o -iname \*.jpeg -o -iname \*.png \) -exec mogrify -path "$output_folder" -resize 100% -quality 70% {} \;

