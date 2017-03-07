__author__ = 'alipirani'
import os
from config_settings import ConfigSectionMap
from modules.log_modules import keep_logging
from modules.logging_subprocess import *
from sys import platform as _platform

<<<<<<< HEAD
=======
<<<<<<< HEAD
def bamqc(out_sorted_bam, out_path, analysis, logger, Config):
    qualimap_base_command = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("qualimap", Config)['qualimap_bin'] + "/" + ConfigSectionMap("qualimap", Config)['base_cmd']
    qualimap_bam_qc_cmd = "%s bamqc -bam %s -outdir %s -outfile %s_report.pdf -outformat pdf" % (qualimap_base_command, out_sorted_bam, out_path, analysis)
    keep_logging("COMMAND: " + qualimap_bam_qc_cmd, qualimap_bam_qc_cmd, logger, 'debug')
    try:
        call(qualimap_bam_qc_cmd, logger)
=======




>>>>>>> d567014e041f722948bec9a7ff6c5e339de749f6
def bamqc(out_sorted_bam, out_path, analysis, logger, Config):
    qualimap_base_command = ConfigSectionMap("bin_path", Config)['binbase'] + "/" + ConfigSectionMap("qualimap", Config)['qualimap_bin'] + "/" + ConfigSectionMap("qualimap", Config)['base_cmd']
    qualimap_bam_qc_cmd = "%s bamqc -bam %s -outdir %s -outfile %s_report.pdf -outformat pdf" % (qualimap_base_command, out_sorted_bam, out_path, analysis)
    keep_logging(qualimap_bam_qc_cmd, qualimap_bam_qc_cmd, logger, 'debug')
    try:
        call(qualimap_bam_qc_cmd, logger)
        #print ""
>>>>>>> 02b125e3d68903b94aba39c984cecc3b7d770e55
    except sp.CalledProcessError:
        keep_logging('Error in Qualimap step. Exiting.', 'Error in Qualimap step. Exiting.', logger, 'exception')
        sys.exit(1)
    qualimap_report_file = "%s/%s_report.pdf" % (out_path, analysis)
    keep_logging('Qualimap Report: {}'.format(qualimap_report_file), 'Qualimap Report: {}'.format(qualimap_report_file), logger, 'debug')
    return qualimap_report_file
