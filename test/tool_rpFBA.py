#!/usr/bin/env python3
"""
Created on September 21 2019

@author: Melchior du Lac
@description: Galaxy script to query rpFBA REST service


python tool_rpFBA.py -inputTar test_input.tar -inSBML test_inSBML.sbml -sim_type fraction -reactions biomass RP1_sink -coefficients 0 0 -isMax True -fraction_of 0.95 -outputTar test_output.tar -dontMerge False -pathway_id rp_pathway -compartment_id MNXC3 -fill_orphan_species False

python tool_rpFBA.py -sbml test_rpCofactors.sbml -inSBML test_inSBML.sbml -sim_type fraction -reactions biomass RP1_sink -coefficients 0 0 -isMax True -fraction_of 0.95 -outputTar test_output.tar -dontMerge False -pathway_id rp_pathway -compartment_id MNXC3 -fill_orphan_species False
"""
import argparse
import sys
import logging
import tempfile
import tarfile

#sys.path.insert(0, '/home/')
import rpToolServe

##
#
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Python wrapper to calculate FBA to generate rpFBA collection')
    parser.add_argument('-inputTar', type=str)
    parser.add_argument('-sbml', type=str)
    parser.add_argument('-inSBML', type=str)
    parser.add_argument('-sim_type', type=str)
    parser.add_argument('-reactions', type=str, nargs='*')
    parser.add_argument('-coefficients', type=str, nargs='*')
    parser.add_argument('-isMax', type=str)
    parser.add_argument('-fraction_of', type=str)
    parser.add_argument('-outputTar', type=str)
    parser.add_argument('-dontMerge', type=str)
    parser.add_argument('-pathway_id', type=str)
    parser.add_argument('-compartment_id', type=str)
    parser.add_argument('-fill_orphan_species', type=str)
    params = parser.parse_args()
    if params.sbml=='None' or params.sbml==None or params.sbml=='':
        if params.inputTar=='None' or params.inputTar==None or params.inputTar=='':
            logging.error('Cannot have no SBML and no TAR input')
            exit(0)
        rpToolServe.main(params.inputTar, 
                params.inSBML,
                params.outputTar,
                params.sim_type,
                params.reactions,
                params.coefficients,
                params.isMax,
                params.fraction_of,
                params.dontMerge,
                params.pathway_id,
                params.fill_orphan_species,
                params.compartment_id)
    else:
        #make the tar.xz 
        with tempfile.TemporaryDirectory() as tmpOutputFolder:
            inputTar = tmpOutputFolder+'/tmp_input.tar.xz'
            with tarfile.open(inputTar, mode='w:xz') as tf:
                tf.add(params.sbml)
            rpToolServe.main(inputTar, 
                    params.inSBML,
                    params.outputTar,
                    params.sim_type,
                    params.reactions,
                    params.coefficients,
                    params.isMax,
                    params.fraction_of,
                    params.dontMerge,
                    params.pathway_id,
                    params.fill_orphan_species,
                    params.compartment_id)
