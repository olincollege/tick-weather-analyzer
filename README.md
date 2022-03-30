# tick-weather-analyzer
## Description

This repository obtains data from the National Ecological Observatory Network, and uses said data to perform an analysis of the impact of relative humidity and precipitation on tick populations at the Harvard Forest & Quabbin Watershed, a NEON field site managed by Harvard University. In order to do so, the tick population, relative humidity, and precipitation data are accessed from NEON using an API.

## Getting Started

### Local Setup
1. Clone the repository.
    `git clone https://github.com/olincollege/tick-weather-analyzer.git`
2. Navigate to the local repository using your terminal.
    ex: `cd tick-weather-analyzer`
3. Install the dependencies listed below if they are not already installed.

### Dependencies
This project relies upon the following dependencies:
* Pandas
    * `pip install pandas`
* Matplotlib
    * `pip install matplotlib`
* NumPy
    * `pip install numpy`
* Requests
    * `pip install requests`

### Executing program
In order to view the analysis of the datasets, the data must be downloaded in your local repository. In order to do so, simply run each cell of the Jupyter notebook in sequential order. Once you have downloaded the data, avoid running the third cell of the notebook as this will result in downloading a second copy of the data. Once downloaded, the data will appear in folders according to the name of the data product ID. The necessary files for each month for the given dataset will appear within each folder.
* Run each cell in the Jupyter Notebook in sequential order.
* To change the datasite or the date range, modify the values defined in the first cell of the notebook.

### Authors
Cherry Pham, Lili Baker, and Tara Lee
