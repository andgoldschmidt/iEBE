#! /usr/bin/env bash
(cd ..
for ii in VISHNew iSS iS osc2u urqmd
  do
  (cd $ii; make; make clean)
done

# build superMC, trento (submodules)
for ii in trento/src superMC; do 
  ( cd $ii;
    if [ ! -d "build" ]; then
      mkdir build
    fi
    cd build
    cmake ../ && make
    name=`echo $ii | cut -d / -f 1`
    mv src/${name}*  ../${name}.e
  )
done

echo "Compiling finished."
echo "Next generate jobs using generate-jobs-XXX.sh."
)
