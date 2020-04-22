Feature: Edit Gits 
as user, i want to edit an existing gits

Scenario: Edit exsiting gits
Given Log in as user to access gits
When click button see all gits to edit
And choose one gits to edit
And click button edit gits
And Edit text area
And click button update public gist
Then i should be successfully edit gits
# And choose type invoice SCSF
# And click button preview
# And click checkbox invoice SCSF
# Then click button submit and should be successfully