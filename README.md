<h1>http://127.0.0.1:8000-API Documentation/</h1><br>

<h1>POST:http://127.0.0.1:8000/user/auth/token</h1><br>
This api is used for generating the token for the user<br>
Request Body:<br>
{<br>
  "email": "user@example.com",<br>
  "password": "string"<br>
}<br>
Response:<br>
{<br>
  "token": "string",<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "id": number<br>
}<br>
STATUS:200_OK<br>

<h1>POST:http://127.0.0.1:8000/user/create</h1><br>
It only creates normal user<br>
Request Body:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringst"<br>
}<br>
Response:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>
STATUS:201_CREATED<br>

<h1>POST:http://127.0.0.1:8000/hackathon/create</h1><br>
It only creates a hackathon if the user is admin user<br>
In the header add the field of authorization:Token yourtoken<br>
Request Body:<br>
{<br>
  "title": "string",<br>
  "description": "string",<br>
  "background_image": "string",<br>
  "hackathon_image": "string",<br>
  "submission_type": "image",<br>
  "start_datetime": "2023-08-02T11:15:09.057Z",<br>
  "end_datetime": "2023-08-02T11:15:09.057Z",<br>
  "reward_prize": "-534972"<br>
}<br>
Response:<br>
{<br>
  "id": 0,<br>
  "title": "string",<br>
  "description": "string",<br>
  "background_image": "string",<br>
  "hackathon_image": "string",<br>
  "submission_type": "image",<br>
  "start_datetime": "2023-08-02T11:15:09.062Z",<br>
  "end_datetime": "2023-08-02T11:15:09.062Z",<br>
  "reward_prize": "539.4"<br>
}<br>
STATUS:201_CREATED<br>

<h1>GET:http://127.0.0.1:8000/hackathon/get/all</h1><br>
It returns the all hackathons if the user is authenticated<br>
In the header add the field of  authorization:Token yourtoken<br>
Request Body:<br>
No request Body<br>
Response:<br>
[<br>
  {<br>
    "id": 0,<br>
    "title": "string",<br>
    "description": "string",<br>
    "background_image": "string",<br>
    "hackathon_image": "string",<br>
    "submission_type": "image",<br>
    "start_datetime": "2023-08-02T11:17:33.454Z",<br>
    "end_datetime": "2023-08-02T11:17:33.454Z",<br>
    "reward_prize": "-805577."<br>
  }<br>
]<br>
STATUS:200_OK<br>

<h1>POST:http://127.0.0.1:8000/register-hackathon/create</h1><br>
It used to register a new hackathon<br>
In the header add the field of  authorization:Token yourtoken<br>
Request Body:<br>
{<br>
  "hackathon": 0<br>
}<br>
Response Body:<br>
{<br>
  "hackathon": 0<br>
}<br>
STATUS:201_CREATED<br>

<h1>GET:http://127.0.0.1:8000/register-hackathon/get/all</h1><br>
It is used to retrieve all the hackathons that the user registered<br>
In the header add the field of  authorization:Token yourtoken<br>
Request Body:<br>
No request Body<br>
Response:<br>
[<br>
  {<br>
    "id": 0,<br>
    "title": "string",<br>
    "description": "string",<br>
    "background_image": "string",<br>
    "hackathon_image": "string",<br>
    "submission_type": "image",<br>
    "start_datetime": "2023-08-02T11:17:33.454Z",<br>
    "end_datetime": "2023-08-02T11:17:33.454Z",<br>
    "reward_prize": "-805577."<br>
  }<br>
]<br>
STATUS:200_OK<br>

<h1>POST-http://127.0.0.1:8000/hackathon-submission/create</h1><br>
It is used to create new submission related to the hackathon<br>
In the header add the field of  authorization:Token yourtoken<br>
Request Body:<br>
{<br>
  "name": "string",<br>
  "summary": "string",<br>
  "submission_file": "string",<br>
  "submission_image":"string",<br>
  "submission_link": "string",<br>
  "hackathon": 0<br>
}<br>
Response:<br>
{<br>
  "id": 0,<br>
  "name": "string",<br>
  "summary": "string",<br>
  "submission_file": "string",<br>
  "submission_image":"string",<br>
  "submission_link": "string",<br>
  "hackathon": 0<br>
}<br>
STATUS:201_CREATED<br>

<h1>GET-http://127.0.0.1:8000/hackathon-submission/get/all</h1><br>
It is used to retrieve all the submissions that user created or made to the hackathons<br>
In the header add the field of  authorization:Token yourtoken<br>
Request Body:<br>
No request Body<br>
Response:<br>
[<br>
{<br>
  "id": 0,<br>
  "name": "string",<br>
  "summary": "string",<br>
  "submission_file": "string",<br>
  "submission_image":"string",<br>
  "submission_link": "string",<br>
  "hackathon": 0<br>
}<br>
]<br>
STATUS:200_OK<br>
