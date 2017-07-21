# < Supply Sergeant >

# Pre-work - *supply sergeant proof of concept*

**Supply Sergeant** is a computer inventory and user request tracker.

Submitted by: **Ben Altieri**

Time spent: **40** hours spent in total

## REST API Endpoints

* [x] GET /items &nbsp;&nbsp;&nbsp;&nbsp; Returns a list of all items in the database
* [x] GET /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Returns a specific item by name
* [x] POST /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Inserts an item into the database by item name with assignee and date assigned
* [x] PUT /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Updates an item by item name and new assignee name keeping previous assignee record
* [x] DEL /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Deletes an item by name
* [x] POST /auth &nbsp;&nbsp;&nbsp;&nbsp; Generates a JWT authentication token
* [x] POST /register &nbsp;&nbsp;&nbsp;&nbsp; For user registration
* [x] GET /inventory/< name >  &nbsp;&nbsp;&nbsp;&nbsp; Get an inventory by name
* [x] POST /inventory/< name >  &nbsp;&nbsp;&nbsp;&nbsp; Create an inventory by name
* [x] DELETE /inventory/< name >  &nbsp;&nbsp;&nbsp;&nbsp; Delete an inventory by name
* [x] GET /inventories  &nbsp;&nbsp;&nbsp;&nbsp; Retrieve a list of all inventories in the system

## User Stories

The following **required** functionality is yet to be completed:

* [x] Design / Define REST API resource methods
* [ ] Define / separate out REST API resources from models
* [ ] REST API resources are external representations of application endpoints, i.e. what the client sees
* [ ] Models are internal representations of objects that are not externally exposed, i.e. the client has no reference to it
* [ ] technician can **create, read, update, delete computer inventory**.
* [ ] technician can **add users to the database** to and from PostgreSQL database called sargdb via sqlalchemy.
* [ ] a user object is created on date of hire.
* [ ] a technician can upload only one picture of computer serial number per computer object.
* [ ] a computer object can only have one mac address.
* [ ] cost of equipment purchase and any subsequent repairs / modifications will be tracked
* [ ] each user will have a profile that lists all issued hardware and software, date of purchase.
* [ ] Invoice .pdf files can be uploaded and related to any costs entered into the system.


The following **additional** features are **to be** implemented:

* [ ] Purchase request approval workflow [ i.e someone requests a new computer, that will trigger an email to the CAPEX committee]

## Mockup on Balsamiq:

<img src='https://autodidactica.mybalsamiq.com/mockups/5883960.png?key=0944258a85141fb06484b669a7cf3b95451f585e' title='Supply Sergeant Mockup' width='' alt='Supply Sergeant Mockup' />

## Video Walkthrough 

Here's a walkthrough of implemented user stories:

<img src='https://www.google.com' title='Video Walkthrough' width='' alt='Video Walkthrough' />

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## Notes

Describe any challenges encountered while building the app.
* [1] Getting the original text to populate over to the edit Activity
* [2] Updating the item and positioning of the ArrayList when a particular item has been updated
* [3] Refactoring code and seeing what overlaps may be

## License

    Copyright [2017] [Ben Altieri]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
