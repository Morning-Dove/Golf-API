# Golf-API



## Models

**Course**

Attributes:
* id (uuid)
* name (string)
* location (string)
* holes (integer)

**Player**

Attributes:
* id (uuid)
* name (string)
* handicap (float)


## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve  collection | GET    | /golf
Retrieve  member     | GET    | /golf/*\<id\>*
Create  member       | POST   | /golf
Update  member       | PUT    | /golf/*\<id\>*
Delete  member       | DELETE | /golf/*\<id\>*
