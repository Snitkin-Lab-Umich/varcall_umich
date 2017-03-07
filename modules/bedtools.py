__author__ = 'alipirani'

import os
from config_settings import ConfigSectionMap
<<<<<<< HEAD
from modules.logging_subprocess import *
from modules.log_modules import *

def bedtools(out_sorted_bam, out_path, analysis, logger, Config):
    base_cmd = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("bedtools", Config)['bedtools_bin'] + "/" + ConfigSectionMap("bedtools", Config)['base_cmd']
    cmd = "%s genomecov -ibam %s -d > %s/%s_coverage.bed" % (base_cmd, out_sorted_bam, out_path, analysis)
    keep_logging("COMMAND: " + cmd, cmd, logger, 'debug')
    try:
        call(cmd, logger)
    except sp.CalledProcessError:
        keep_logging('Error in Bedtools unmapped step. Exiting.', 'Error in Bedtools unmapped step. Exiting.', logger, 'exception')
        sys.exit(1)
    final_coverage_file = "%s/%s_coverage.bed" % (out_path, analysis)
    return final_coverage_file


# def parse_bed_file(final_bed_unmapped_file):
#     unmapped_positions_array = []
#     with open(final_bed_unmapped_file, 'rU') as fp:
#         for line in fp:
#             line_array = line.split('\t')
# 	    lower_index = int(line_array[1]) + 1
#             upper_index = int(line_array[2]) + 1
#             for positions in range(lower_index,upper_index):
#                 unmapped_positions_array.append(positions)
#     only_unmapped_positions_file = final_bed_unmapped_file + "_positions"
#     f1=open(only_unmapped_positions_file, 'w+')
#     for i in unmapped_positions_array:
#         p_string = str(i) + "\n"
#         f1.write(p_string)
#     return only_unmapped_positions_file
=======
from modules.bioawk import *
from modules.logging_subprocess import *
from modules.log_modules import *


def bedtools(out_sorted_bam, out_path, analysis, logger, Config):
    base_cmd = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("bedtools", Config)['bedtools_bin'] + "/" + ConfigSectionMap("bedtools", Config)['base_cmd']
    cmd = "%s genomecov -ibam %s -bga | awk '$4==0' > %s/%s_unmapped.bed" % (base_cmd, out_sorted_bam, out_path, analysis)
    keep_logging(cmd, cmd, logger, 'debug')
    try:
        call(cmd, logger)
        #print ""
    except sp.CalledProcessError:
        keep_logging('Error in Bedtools unmapped step. Exiting.', 'Error in Bedtools unmapped step. Exiting.', logger, 'exception')
        sys.exit(1)
    final_bed_unmapped_file = "%s/%s_unmapped.bed" % (out_path, analysis)
    only_unmapped_positions_file = parse_bed_file(final_bed_unmapped_file)
    return only_unmapped_positions_file





def parse_bed_file(final_bed_unmapped_file):
    unmapped_positions_array = []
    with open(final_bed_unmapped_file, 'rU') as fp:
        for line in fp:
            line_array = line.split('\t')
            lower_index = int(line_array[1]) + 1
            upper_index = int(line_array[2]) + 1
            for positions in range(lower_index,upper_index):
                unmapped_positions_array.append(positions)
    only_unmapped_positions_file = final_bed_unmapped_file + "_positions"
    f1=open(only_unmapped_positions_file, 'w+')
    for i in unmapped_positions_array:
        p_string = str(i) + "\n"
        f1.write(p_string)
    return only_unmapped_positions_file

def bedgraph_coverage(out_sorted_bam, out_path, analysis, reference, logger, Config):
    reference_SIZE_file = bioawk_make_reference_size(reference, logger, Config)
    reference_filename_base = os.path.basename(reference)
    reference_first_part_split = reference_filename_base.split('.')
    first_part = reference_first_part_split[0]
    reference_dir = os.path.dirname(reference)
    makewindows_cmd = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("bedtools", Config)['bedtools_bin'] + "/" + ConfigSectionMap("bedtools", Config)['version_for_coverage'] + ConfigSectionMap("bedtools", Config)['base_cmd'] + " makewindows -g %s -w 1000 > %s/%s.bed" % (reference_SIZE_file, reference_dir, first_part)
    keep_logging(makewindows_cmd, makewindows_cmd, logger, 'debug')
    try:
        call(makewindows_cmd, logger)
        #print ""
    except sp.CalledProcessError:
        keep_logging('Error in Bedtools Make Windows step. Exiting.', 'Error in Bedtools Make Windows step. Exiting.', logger, 'exception')
        sys.exit(1)
    reference_windows_file = "%s/%s.bed" % (reference_dir, first_part)
    bedcoverage_command = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("bedtools", Config)['bedtools_bin'] + "/" + ConfigSectionMap("bedtools", Config)['version_for_coverage'] + ConfigSectionMap("bedtools", Config)['base_cmd'] + " coverage -abam %s -b %s > %s/%s.bedcov" % (out_sorted_bam, reference_windows_file, out_path, analysis)
    keep_logging(bedcoverage_command, bedcoverage_command, logger, 'debug')
    try:
        call(bedcoverage_command, logger)
        #print ""
    except sp.CalledProcessError:
        keep_logging('Error in Bedtools coverage step. Exiting.', 'Error in Bedtools coverage step. Exiting.', logger, 'exception')
        sys.exit(1)









>>>>>>> 02b125e3d68903b94aba39c984cecc3b7d770e55
