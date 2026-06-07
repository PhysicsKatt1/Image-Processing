# Image-Processing

A collection of Python scripts for image-based measurement analysis, ROI selection, and image quality evaluation. These tools were developed for processing large batches of microscopy or metrology images, extracting region-of-interest (ROI) statistics, calculating contrast-to-noise ratios (CNR), and consolidating results for further analysis.

## Overview

This repository currently contains three scripts:

| Script | Purpose |
|----------|----------|
| `ImProc_ROIselAndStats_UniformSpotSize.py` | ROI selection and image statistics using a fixed ROI radius |
| `ImProc_ROIselAndStats_DynamicSpotSize.py` | ROI selection and image statistics using a user-defined ROI radius for each image |
| `ImProc_ConcatAndMatchCSVs_DynamicSpotSize.py` | Combines image statistics CSVs and matches results with external measurement data |

---

## Features

- Batch image processing
- Automatic TIFF to JPEG conversion
- Interactive ROI selection
- Fixed-size and variable-size ROI workflows
- ROI and background intensity measurements
- Contrast-to-noise ratio (CNR) calculations
- Batch statistics export to CSV
- Consolidation of image statistics across datasets
- Correlation of image metrics with external measurement data

---

## Requirements

Install required packages:

```bash
pip install numpy pandas opencv-python pillow glob2
```

### Dependencies

- numpy
- pandas
- opencv-python
- pillow
- glob2

---

## Repository Structure

```text
image-processing/
│
├── ImProc_ROIselAndStats_UniformSpotSize.py
├── ImProc_ROIselAndStats_DynamicSpotSize.py
├── ImProc_ConcatAndMatchCSVs_DynamicSpotSize.py
│
├── Images/
│   ├── image_001.tif
│   ├── image_002.tif
│   └── ...
│
├── JPEGS/
│   ├── image_001.jpeg
│   ├── image_002.jpeg
│   └── ...
│
└── ImageStats.csv
```

---

## ROI Selection Scripts

### ImProc_ROIselAndStats_UniformSpotSize.py

Processes a batch of images using a fixed ROI radius.

### Workflow

1. Convert TIFF images to JPEG format.
2. Open each image sequentially.
3. Left-click the center of the feature of interest.
4. A circular ROI mask is applied using a predefined radius.
5. Press `ESC` to continue to the next image.
6. Statistics are calculated and saved.

### Calculated Metrics

- ROI Mean Intensity
- ROI Standard Deviation
- Background Mean Intensity
- Background Standard Deviation
- Total Image Mean
- Total Image Standard Deviation
- Contrast-to-Noise Ratio (CNR)

### Output

```text
ImageStats.csv
```

---

### ImProc_ROIselAndStats_DynamicSpotSize.py

Processes images where feature size varies between images.

### Workflow

1. Convert TIFF images to JPEG format.
2. Open image.
3. Left-click to define ROI center.
4. Right-click on the ROI edge to define radius.
5. Circular ROI is generated dynamically.
6. Statistics are calculated and exported.

### Additional Output

The dynamically selected ROI radius is saved for each image.

Output columns include:

```text
file
radius
ROImean
ROIstddev
backgroundMean
backgroundStddev
totalMean
totalStddev
cnr
```

---

## Data Consolidation Script

### ImProc_ConcatAndMatchCSVs_DynamicSpotSize.py

Combines multiple CSV outputs generated from dynamic ROI analysis and associates image-derived statistics with external measurement data.

### Workflow

1. Load all CSV files from a target directory.
2. Concatenate results into a single dataset.
3. Load external Excel data.
4. Prepare filenames for matching.
5. Enable downstream correlation and statistical analysis.

### Intended Use

Useful for studies comparing:

- Imaging parameters
- Tool settings
- Detection thresholds
- Measurement performance
- Signal quality metrics

---

## Contrast-to-Noise Ratio (CNR)

The scripts calculate CNR using:

\[
CNR = \frac{|ROI_{mean} - Background_{mean}|}
{\sqrt{ROI_{std}^2 + Background_{std}^2}}
\]

Higher CNR values indicate improved feature visibility relative to background noise.

---

## Example Workflow

### 1. Prepare Images

Place TIFF images in a working directory:

```text
Images/
```

### 2. Run ROI Selection

For fixed feature sizes:

```bash
python ImProc_ROIselAndStats_UniformSpotSize.py
```

For varying feature sizes:

```bash
python ImProc_ROIselAndStats_DynamicSpotSize.py
```

### 3. Review Output

Results are saved as:

```text
ImageStats.csv
```

### 4. Consolidate Results

```bash
python ImProc_ConcatAndMatchCSVs_DynamicSpotSize.py
```

---

## Applications

- Semiconductor inspection
- Microscopy image analysis
- Optical metrology
- Defect detection studies
- Signal-to-noise investigations
- Tool parameter optimization
- Image quality assessment
- Process development and characterization

---

## Future Enhancements

Potential future improvements include:

- Automated ROI detection
- Batch processing without user interaction
- Additional image quality metrics
- Segmentation-based analysis
- Multi-ROI support
- Interactive visualization dashboards
- Statistical reporting notebooks

---

## License

MIT License
