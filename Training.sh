#!/bin/bash

# التحقق مما إذا كان المتغير $1 موجودًا
if [ -z "$1" ]; then
  echo "Error: MODEL_NAME is not specified."
  echo "Usage: $0 <MODEL_NAME>"
  exit 1
fi

# تنفيذ الأوامر إذا كان المتغير $1 موجودًا
python3.10 Training/t2i.py
cd Training/tesstrain
TESSDATA_PREFIX=../tessdata make training MODEL_NAME=$1 TESSDATA=../tessdata START_MODEL=eng UNICHARSET=unicharset MAX_ITERATIONS=1000
cp data/$1.traineddata ../tessdata/

