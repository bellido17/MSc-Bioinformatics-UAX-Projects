#!/bin/bash

# Script reproducible para la anotación de variantes con VEP (offline + cache)

# Comprobamos que se pase un archivo VCF como argumento
if [ $# -ne 1 ]; then
  echo "Uso: ./run_vep.sh <archivo_vcf>"
  exit 1
fi

INPUT_VCF=$1
OUTPUT_FILE="ID_Patient_exome_annotated.txt"
CACHE_DIR="$HOME/vep_data"

docker run --rm -it \
  -v $HOME:/data \
  -v $CACHE_DIR:/opt/vep/.vep \
  ensemblorg/ensembl-vep \
  vep \
    -i /data/$INPUT_VCF \
    -o /data/$OUTPUT_FILE \
    --species homo_sapiens \
    --assembly GRCh38 \
    --offline \
    --cache \
    --dir_cache /opt/vep/.vep \
    --vcf \
    --hgvs \
    --symbol \
    --sift b \
    --polyphen b \
    --af \
    --variant_class \
    --everything
