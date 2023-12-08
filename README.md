# datascience_practice_python

This repository serves as a comprehensive resource for anyone eager to delve into the world of Python programming. Divided into two distinct parts, it provides a structured learning experience. 
* The first part features a collection of Jupyter files within the 'practice_python' folder, offering a hands-on and interactive environment for Python practice. These files cover a myriad of topics, from foundational concepts to advanced exercises, facilitating a gradual mastery of the language.
* In the second part, a robust Flask project awaits exploration, showcasing the practical application of Python in a real-world scenario. With features spanning user management, location tracking, company operations, position handling, and user-company mappings, this Flask RESTful API project offers valuable insights into building scalable and functional applications.

Whether you're a novice honing your Python skills or an experienced developer seeking practical examples, this repository caters to a diverse audience eager to enhance their programming proficiency.

# Python Practice
Explore the 'practice_python' folder to find Jupyter files for Python practice. 
1. Python Basics
2. Data Structures in Python
3. Data Manipulation and Visualization
   
You can run these files using Jupyter Notebook.

# Flask RESTful API Project
## Overview
This project is a Flask RESTful API that provides endpoints for managing users, locations, companies, positions, and user-company mappings. It follows best practices for structuring a Flask project and includes unit tests using pytest.

## Features
* User management (CRUD operations)
* Location management (CRUD operations)
* Company management (CRUD operations)
* Position management (CRUD operations)
* User-Company Mapping management (CRUD operations)

## Getting Started
1. Install software: docker
2. Pull the image:
  ```
  docker pull taranjitkaurme/datascience_practice_python:latest
  ```

3. Run the Docker container:
  ```
  docker run -p 5000:5000 taranjitkaurme/datascience_practice_python:latest
  ```

## Getting Started to contribute
1. Install all the softwares: python, pipenv, docker, intelliJ, git

   Note: You can also use - https://github.com/neurabytes/nb-automation-devtools
   
2. Clone the repository:
  ```
  git clone https://github.com/taranjitkaurmee/datascience_practice_python.git
  cd datascience_practice_python
  ```
3. Install dependencies:  
  ```  
  pipenv install
  ```

4. Run the Flask application:
  ```
  python app.py
  ```
The API will be accessible at http://localhost:5000.

## API Endpoints
* Users:
  * GET: /api/users
  * GET: /api/users/<int:user_id>
  * POST: /api/users
  * PUT: /api/users/<int:user_id>
  * DELETE: /api/users/<int:user_id>
    
* Locations:
  * GET: /api/location
  * GET: /api/location/<int:location_id>
  * POST: /api/location
  * PUT: /api/location/<int:location_id>
  * DELETE: /api/location/<int:location_id>
    
* Companies:
  * GET: /api/company
  * GET: /api/company/<int:company_id>
  * POST: /api/company
  * PUT: /api/company/<int:company_id>
  * DELETE: /api/company/<int:company_id>
    
* Positions:
  * GET: /api/position
  * GET: /api/position/<int:position_id>
  * POST: /api/position
  * PUT: /api/position/<int:position_id>
  * DELETE: /api/position/<int:position_id>
    
* User-Company Mappings:
  * GET: /api/usercompanymapping
  * GET: /api/usercompanymapping/<int:mapping_id>
  * POST: /api/usercompanymapping
  * PUT: /api/usercompanymapping/<int:mapping_id>
  * DELETE: /api/usercompanymapping/<int:mapping_id>

## Testing
Run unit tests using pytest:
  ```
  pytest
  ```
## Contributing
Feel free to contribute by reporting issues, suggesting enhancements, or submitting pull requests. 

## License
This project is licensed under the MIT License - see the LICENSE file for details.
