# Diabetes Dataset Analysis

An exploratory data analysis (EDA) project on a diabetes dataset, using automated profiling to quickly surface data quality issues, distributions, correlations, and missing values.

## Aims & Goals
In this project, I will analyze the Diabetes Dataset, which contains medical and demographic information related to diabetes.
The goal is to explore the dataset and uncover any patterns, correlations, and potential issues such as missing values or outliers.

## Overview

This project generates a comprehensive profiling report for the diabetes dataset using [ydata-profiling](https://github.com/ydataai/ydata-profiling) (formerly pandas-profiling). The report provides a fast, thorough first pass at understanding the data before deeper analysis or modeling.

## Features

- Automated exploratory data analysis with `ydata-profiling`
- Generates an interactive report covering:
  - Variable types, distributions, and summary statistics
  - Missing value analysis
  - Correlations between features
  - Duplicate row detection
  - Warnings for data quality issues (e.g. high cardinality, skewness, zeros)
- Report can be viewed inline in the notebook or exported as a standalone HTML file

## Requirements

- Python 3.x
- `ydata-profiling`

Install the dependency with:

```bash
pip install ydata-profiling
```

> **Note:** `ydata-profiling` is under active development and package names/APIs may change. If you run into a deprecation warning, check the [ydata-profiling docs](https://docs.profiling.ydata.ai/) for the latest install instructions.

## Usage

Open `diabetes.ipynb` in [Google Colab](https://colab.research.google.com/github/TeeMiles01/Data-Science-projects/blob/main/diabetes-project/diabetes.ipynb) or Jupyter Notebook, then run the cells from top to bottom.

The notebook will:
1. Load the diabetes dataset
2. Generate a `ProfileReport`
3. Display the report inline in the notebook
4. Optionally save the report as `diabetes_profiling_report.html` for sharing or offline viewing

## Output

The generated HTML report (`diabetes_profiling_report.html`) can be opened in any web browser and includes an overview, variable-by-variable breakdown, correlation heatmaps, and a sample of the data.

## License

Feel free to use, modify, and share this project.
