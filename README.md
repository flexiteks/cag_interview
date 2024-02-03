# cag_interview

### Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

   
2. Run on Docker:

   docker-compose build
   docker-compose up


### Tests

1. Postman
    Do a post request to the following links on Postman after docker has successfully running the file

    http://127.0.0.1:5000/api/insert-update-inventory
    http://127.0.0.1:5000/api/get-inventory-in-timeframe
    http://127.0.0.1:5000/api/aggregate-inventory


2. run pytest.py
    run on CMD 

    python py_tests.py
