# autonomous-snow-vehicle-IOT
# Snow Terrain Mobility Monitoring

This project analyzes sensor data from an autonomous vehicle to monitor and evaluate
mobility performance in snowy and low-traction environments.

# Project Goals
- Monitor traction stability using sensor data
- Detect slip and directional drift
- Visualize mobility performance
- Deploy results on AWS EC2

# Repository Structure
- data      : Raw and processed datasets
- notebooks   : Data analysis and modeling notebooks
- dashboards  : Streamlit dashboard
- models      : Saved models
- docs       : Project report and documentation

    data/

         └── raw/

               └── snow_terrain_mobility_raw.csv
  ## Data Resources
The project uses a public-style terrain mobility dataset containing IMU, wheel encoder,
and temperature data. Although the dataset is adapted, low-traction behavior is interpreted
as snow and icy terrain conditions for mobility analysis.

            


