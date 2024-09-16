# System Health Monitoring

## Overview

This project monitors server health, visualizes metrics, and sends notifications. It uses Python for backend tasks and Dash for a web-based dashboard.

## Setup

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set Up the Database**
   ```python
   from database.db_utils import create_table_if_not_exists

   db_filename = 'servers.db'
   create_table_if_not_exists(db_filename)

6. **Import Server Data**
   Prepare a CSV file named servers.csv with columns hostname and ip.
   Import data into the database
   ```python
   from database.db_utils import insert_servers_from_csv

   csv_filename = 'servers.csv'
   insert_servers_from_csv(csv_filename, db_filename)

### Running the Application
**Start the Web Dashboard**

**To run the web application and view the dashboard**:
python app.py
Access the dashboard at http://localhost:8050

# Features
## Real-Time Monitoring
  View CPU, memory, and disk usage metrics.
## Visualizations
  Interactive graphs for server performance.
## Anomaly Detection
  Detect and highlight anomalies in system metrics.
## Notifications
  Send alerts via email and Microsoft Teams.
## Automatic Cleanup
  Perform disk cleanup if usage exceeds a threshold.

### Code Overview
database/db_utils.py: Functions for database operations.

create_table_if_not_exists(db_filename): Creates the servers table.
insert_servers_from_csv(csv_filename, db_filename): Imports server data from a CSV file.
utils/data.py: Generates sample data for testing.

generate_sample_data(server_name): Creates synthetic data for a given server.
app.py: Initializes the Dash web application and handles interactive visualizations.

plot/figures.py: Contains functions for generating charts and graphs.

Contributing
Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes.
Commit and push: git commit -am 'Add new feature', git push origin feature-branch.
Open a Pull Request.
### License
MIT License - see the LICENSE file for details.

### Contact
For questions, open an issue on GitHub or email your-email@example.com.

