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
- docs       : Project report and documentation

 Dataset file:
             
              data/raw/snow_terrain_mobility_raw.csv

  ## Data Resources
The project uses a public-style terrain mobility dataset containing IMU, wheel encoder,
and temperature data. Although the dataset is adapted, low-traction behavior is interpreted
as snow and icy terrain conditions for mobility analysis.
## How to Run

1. Clone the repository
2. Open the notebooks/ folder
3. Run the notebook:
   01_exploratory_data_analysis.ipynb
4. The notebook automatically loads the dataset and computes mobility metrics.

## How to run app.py

1. Clone repository
2. Install dependencies
   pip install -r requirements.txt
3. Start the server
   python3 app.py
4. Subscribe to MQTT
   mosquitto_sub -h localhost -t snow/data -v

## AWS Deployment

The system was deployed on an AWS EC2 Free Tier Ubuntu instance to simulate cloud-based processing of autonomous vehicle mobility data. Python scripts were executed remotely on the server via SSH, enabling real-time streaming of CSV sensor telemetry to an MQTT broker. Data transmission was verified using Mosquitto subscribers, demonstrating how mobility monitoring can be performed in real robotic IoT systems. Deployment screenshots and verification outputs are provided in the docs/ folder.

## Deliverables

✔ Notebook analysis

✔ Project report (docs/project_report.pdf)

✔ Presentation slides (docs/presentation_slides.pptx)

✔ AWS deployment proof

✔ Clean GitHub repository

## Team

Project by:
Mohamed Amine boubker 231023240
&Mohamed reda berroho 231023239




            


