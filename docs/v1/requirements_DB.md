# Tax-CRM version #1

## Архітектурне рішення бази даних

### Моделі

#### user
 - PK -- id -- INT
 - FK -- user_basic_details
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### user_details
 - PK -- id -- INT
 - _ _ -- first_name -- VARCHAR(40)
 - _ _ -- last_name -- VARCHAR(40)
 - _ _ -- email -- VARCHAR(40)
 - _ _ -- job_title -- VARCHAR(60)
 - _ _ -- phone_number -- VARCHAR(14)
 - _ _ -- address -- VARCHAR(50)
 - _ _ -- url_image -- TEXT
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### lead
 - PK -- id -- INT
 - FK -- lead_details
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### lead_details
 - PK -- id -- INT
 - _ _ -- first_name -- VARCHAR(40)
 - _ _ -- last_name -- VARCHAR(40)
 - _ _ -- ORGANIZATION -- VARCHAR(100)
 - _ _ -- email -- VARCHAR(40)
 - _ _ -- phone_number -- VARCHAR(14)
 - _ _ -- address -- VARCHAR(50)
 - _ _ -- url_image -- TEXT
 - _ _ -- comments -- TEXT
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### activity
 - PK -- id -- INT
 - FK -- lead
 - FK -- activity_details

#### activity_details
 - PK -- id -- INT
 - _ _ -- title -- VARCHAR(40)
 - _ _ -- activity_type -- VARCHAR(40)
 - FK -- user (who_create)
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### communication
 - PK -- id -- INT
 - FK -- lead
 - FK -- communication_details

#### communication_details
 - PK -- id -- INT
 - _ _ -- subject -- VARCHAR(60)
 - _ _ -- text -- TEXT
 - FK -- user (who_send)
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### skills
 - PK -- id -- INT
 - FK -- lead
 - FK -- skills_details

#### skills_details
 - PK -- id -- INT
 - _ _ -- title -- VARCHAR(60)
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime

#### tags
 - PK -- id -- INT
 - FK -- lead
 - FK -- tags_details

#### tags_details
 - PK -- id -- INT
 - _ _ -- title -- VARCHAR(60)
 - _ _ -- datetime_update -- datetime
 - _ _ -- datetime_create -- datetime