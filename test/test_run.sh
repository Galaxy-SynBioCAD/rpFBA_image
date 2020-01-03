#!/bin/sh

docker run --network host -d -p 8888:8888 --name test_rpFBA brsynth/rpfba
sleep 10
python tool_rpFBA.py -inputTar test_input.tar -outputTar test_output.tar -inSBML test_inSBML.sbml -dontMerge True -pathway_id rp_pathway -compartment_id MNXC3 -fillOrphanSpecies False -server_url http://0.0.0.0:8888/REST 
docker kill test_rpFBA
docker rm test_rpFBA
