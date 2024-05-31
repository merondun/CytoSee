#!/usr/bin/env python3
import argparse
import subprocess
import os
import sys

# Version
__version__ = '0.1.2'

def main():
    parser = argparse.ArgumentParser(description='Create CytoSeen 5mC Reproducibility Reports')
    parser.add_argument('--version', action='version', version=f'CytoSeen Version: {__version__}')
    parser.add_argument('--info', required=True, help='Path to the info CSV file')
    parser.add_argument('--min_cov', default=20, type=int, help='Minimum site coverage [default=20]')
    parser.add_argument('--max_cov', default=200, type=int, help='Maximum site coverage [default=200]')
    parser.add_argument('--max_missing', default=0.1, type=float, help='Maximum missing data threshold [default=0.1]')
    parser.add_argument('--outdir', required=True, help='Output directory')
    parser.add_argument('--covdir', required=True, help='Directory to the Bismark coverage files')
    args = parser.parse_args()

    # Resolve absolute paths
    info_path = os.path.abspath(args.info)
    outdir_path = os.path.abspath(args.outdir)
    covdir_path = os.path.abspath(args.covdir)

    # Check if the R script exists at the expected location
    script_path = 'render_report.R'
    if not os.path.exists(script_path):
        print("The file 'render_report.R' does not exist in the expected directory.")
        script_path = input("Please enter the full path to the 'render_report.R' file: ")
        if not os.path.exists(script_path):
            print("render_report.R does not exist at the specified path.", file=sys.stderr)
            sys.exit(1)

    # Run
    command = [
        'Rscript', script_path,  
        '--info', info_path,
        '--min_cov', str(args.min_cov),
        '--max_cov', str(args.max_cov),
        '--max_missing', str(args.max_missing),
        '--outdir', outdir_path,
        '--covdir', covdir_path
    ]

    # Execute render
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to run R script:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    else:
        print(result.stdout)

if __name__ == '__main__':
    main()
