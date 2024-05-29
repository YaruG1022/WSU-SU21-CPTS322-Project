# WSU-SU21-CPTS322-Project

## Setup
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
## Running

To run the **development server**, cd into the src directory and run:
````
flask run
````