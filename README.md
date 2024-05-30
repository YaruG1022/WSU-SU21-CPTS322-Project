# Acme Food Bank Inventory Tracking System
WSU-SU21-CPTS322-Project



## Project summary

### Description of the project
A web application for efficient inventory management of food and hygiene product donations using Python, Flask, HTML, and SQLite.

### Additional information about the project
The Acme Food Bank Inventory Tracking System is designed to address the challenges faced by food banks in managing frequent and varied donations. This system aims to facilitate real-time updates, provide secure user authentication, and generate detailed reports to enhance operational efficiency. It offers a user-friendly interface for managing inventory, tracking donations, updating stock, and processing recipient orders.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

Before you begin, ensure you have the following installed on your machine:
- Git
- Python (version 3.8 or higher)
- SQLite
- Flask

### Add-ons

The project includes the following add-ons:
- **Flask**: For building the web application.
- **SQLite**: For the database to store inventory and user data.


### Installation Steps

#### Setup
Before development, creating a virtual environment is recommended.
To create a virtual environment, run:
````
python -m venv venv
````
then activate it on windows with:
````
.\venv\Scripts\Activate.ps1
````
or on linux by running:
````
source ./venv/bin/activate
````

Then, install all dependencies with:
````
pip install -e .
````
#### Running

To run the **development server**, cd into the src directory and run:
````
flask run
````

## Functionality

To use the Acme Food Bank Inventory Tracking System, follow these steps:

1. **Log In/Sign Up**: Users can sign up for a new account or log in to an existing one.
2. **Dashboard**: Upon logging in, users are taken to the dashboard which provides an overview of inventory levels, recent donations, and upcoming expirations.
3. **Add New Donation**: Navigate to the "Add Donation" page to enter details of new donations and update the inventory.
4. **Update Inventory**: Modify existing inventory items by navigating to the "Update Inventory" page.
5. **Generate Report**: Create customized reports by selecting the desired parameters on the "Generate Report" page.
6. **Receive Notifications**: Get alerts about items nearing their expiration dates.
7. **Recipient Orders**: Recipients can place their demand requests, which are processed by the system.


## Known Problems

TODO: Describe any known issues, bugs, odd behaviors or code smells. 
Provide steps to reproduce the problem and/or name a file or a function where the problem lives.


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Additional Documentation
We welcome contributions from the community! Follow these steps to contribute:

For more detailed documentation, refer to the following files:
- [Sprint Reports]([docs/sprint_reports.md](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/tree/207cccf6f9f5f89019f01688a4087f6f27e2f1c8/Sprint_Reports))

## License
This project is licensed under the MIT License. See the [LICENSE.txt]([LICENSE.txt](https://choosealicense.com/licenses/mit/)) file for details.
