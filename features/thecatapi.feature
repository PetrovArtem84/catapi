Feature: showing off behave

  Scenario: get scenario for the cat api
     Given we send get request to thecatapi.com and save the response to the context
      Then response code is "200"
      Then response length is more than 0
      When user randomly selects vote record and saves it to context and gets this record by id
      Then response code is "200"
      Then response entity is the same as randomly picked

  Scenario: post/delete scenario for the cat api
     When Create a new vote POST /votes. image_id "asf2", sub_id "my-user1234", value "1"
     Then response code is "200"
     Then response "message" is "SUCCESS"
     Then response "id" is not empty
     When user gets created record by id
     Then response code is "200"
     Then received vote id matches with created
     When user deletes created vote by id
     Then response code is "200"
     Then response "message" is "SUCCESS"
     When user gets created record by id
     Then response code is "404"
