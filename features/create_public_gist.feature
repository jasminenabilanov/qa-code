Feature: Create Public Gist
As user
i want to create a public Gist

Scenario: Create public gist successfully
Given Access URL Gist
When Fill username and password git
And Fill description gist
And Fill filename including extension
And Fill description text area
And click button submit
Then I should see successfully