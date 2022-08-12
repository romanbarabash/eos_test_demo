# Framework setup

### Set env variables
##### Create `.env` file based on `env.example` file (similar for this demo project)

## Installation
##### Install Python
```
Version 3.9 or higher
```
##### Clone project
```
git clone https://github.com/romanbarabash/eos_test_demo.git
```
##### Creating a virtual environment
```
python -m venv venv
```
##### Activating a virtual environment  
Linux or macOS:
```
source venv/bin/activate
```
Windows:
```
.\venv\Scripts\activate
```
##### Installing packages
```
pip install -r requirements.txt
```

##### Run all tests locally

```
pytest --capture=no tests
```

# TODOs
Here are list of TODO features, which are not covered with tech task, 
but good to implement next:
```
- pylint code check
- logging
- reporting tool integration
- test on fail logic with attaching screenshoot and browser logs
- assert matchers pattern
- more advanced strategy of handling page elements
```



