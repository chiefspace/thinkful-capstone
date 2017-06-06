# < Supply Sergeant >

# Pre-work - *supply sergeant proof of concept*

**** is a computer inventory and user request tracker.

Submitted by: **Ben Altieri**

Time spent: **3** hours spent in total

## User Stories

The following **required** functionality is completed:

* [ ] Design / Define REST API resource methods
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

The following **optional** features are implemented:

* [ ] Improve style of the blah blah items in the list [using a custom adapter](http://google.com)
* [ ] Add support for completion due dates for blah blah items (and display within listview item)
* [ ] Use a [DialogFragment](http://google.com) instead of new Activity for editing items


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
