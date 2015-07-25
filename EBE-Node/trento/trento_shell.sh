#! /usr/bin/env bash

cat > parameters.conf << "EOF"
# --------------------------
# Parameters file for TRENTO
# --------------------------
# Output type
quiet = false
output = events
# --------------------------
EOF

./src/trento.e -c parameters.conf "$@"
rm parameters.conf

if [ -d "events" ]; then
  (
    cd events;
    for i in `ls`; do
      index=`echo $i | cut -d\. -f1`;

      # remove commented lines
      sed -n '/^#/!p' < $i > tr_event_${index}_block.dat;

      # include only commented lines, reformat like [ b \n N_part ]
      sed -n '/^#/p' < $i | sed 's/# //' | cut -d = -f 2 | sed -e 's/^[[:space:]]*//' | tail -n +2 > tr_event_${index}_scalars.dat;

      rm $i;
    done;
  )
fi;
