#!/usr/bin/env Rscript

library(optparse)
library(rmarkdown)

option_list <- list(
  make_option(c("--info"), type = "character", default = NULL, help = "Path to input file"),
  make_option(c("--min_cov"), type = "integer", default = 20, help = "Minimum coverage"),
  make_option(c("--max_cov"), type = "integer", default = 200, help = "Maximum coverage"),
  make_option(c("--max_missing"), type = "numeric", default = 0.1, help = "Maximum missing data fraction"),
  make_option(c("--outdir"), type = "character", default = ".", help = "Output directory"),
  make_option(c("--covdir"), type = "character", default = ".", help = "Directory containing coverage files")
)

# Parse options
opt <- parse_args(OptionParser(option_list = option_list))

# Try to find the file in $CONDA_PREFIX/bin
rmd_file <- file.path(Sys.getenv("CONDA_PREFIX"), "bin", "cytoseen.Rmd")

# Check if the file exists at the CONDA_PREFIX/bin location
if (!file.exists(rmd_file)) {
    # If not found, check in the current working directory
    rmd_file <- file.path(getwd(), "cytoseen.Rmd")
    
    if (!file.exists(rmd_file)) {
        # If still not found, prompt the user to enter the path manually
        cat("The file 'cytoseen.Rmd' was not found in $CONDA_PREFIX/bin or the current working directory.\n")
        rmd_file <- readline("Please enter the full path to the cytoseen.Rmd file: ")
        
        if (!file.exists(rmd_file)) {
            stop("cytoseen.Rmd does not exist at the specified path.")
        }
    }
}

# Render the RMarkdown file
rmarkdown::render(rmd_file, params = list(
  info = opt$info,
  min_cov = opt$min_cov,
  max_cov = opt$max_cov,
  max_missing = opt$max_missing,
  outdir = opt$outdir,
  covdir = opt$covdir
), output_file = file.path(opt$outdir, "CytoSeen.html"))