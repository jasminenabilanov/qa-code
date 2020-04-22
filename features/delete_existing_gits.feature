Feature: delete existing gits
As user
i want to delete an existing gits

Scenario: delete gits successfully
Given Log in as user to delete gits
When click button see all gits
And choose gits to delete
And click button delete 
Then i should be successfully deleted