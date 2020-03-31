#!/bin/bash

folder="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set -x

# Creazione ambiene
mkdir -p "$folder"/input
mkdir -p "$folder"/output
rm -r "$folder"/input/*.*
rm -r "$folder"/output/*.*

# Download file CSV dal repository github del Dipartimento Protezione Civile (https://github.com/pcm-dpc/COVID-19)
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv" > "$folder"/input/dpc-covid19-ita-andamento-nazionale.csv
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv" > "$folder"/input/dpc-covid19-ita-regioni.csv
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv" > "$folder"/input/dpc-covid19-ita-province.csv

# Generazione triple RDF
cd src

for i in "$folder"/src/*generator.py; do
  python $i
done