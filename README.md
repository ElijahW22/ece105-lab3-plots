# ECE105 Lab 3 Sensor Plots
Standalone Python script that generates synthetic sensor data and saves scatter, histogram, and box-plot visualizations as a single PNG figure.

## Installation
Activate your `ece105` conda environment, then install dependencies with conda or mamba:

```bash
conda activate ece105
conda install numpy matplotlib
```

or

```bash
conda activate ece105
mamba install numpy matplotlib
```

## Usage
Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output
The script produces one output file:

- `sensor_analysis.png` (150 DPI, tight bounding box), containing:
  - A scatter plot of Sensor A and Sensor B temperature vs. time.
  - An overlaid histogram of Sensor A and Sensor B temperature distributions with dashed mean lines.
  - A side-by-side box plot for Sensor A and Sensor B with a dashed overall-mean line.

## AI tools used and disclosure
[Placeholder: Describe any AI tools used during development (tool name, what was generated/suggested, and what was manually reviewed or modified before submission).]

