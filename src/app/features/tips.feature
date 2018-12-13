Feature: Tips listing
  
   @dev
   Scenario: Tips can be added
    	Given  a user account with the email "example@example.com" exists
    	And    the user "example@example.com" is logged in
    	And    the url is "/tips/"
 
    	When   the user presses the button to add new reading tip
    	And    enters title "test", chooses the type "Website", enters description"test" and enters a webpage "https://www.google.fi"

		And    the tip is submitted
 
    	Then   the page contains the added tip with title "test"
 
 
   @dev
   Scenario: Tips can be removed
        Given  a user account with the email "example@example.com" exists
    	And    the user "example@example.com" is logged in
    	And    the database is initialized for tips_can_be_removed
    	And    the url is "/tips/"
 
    	When   the delete button is pressed
    	Then   the page no longer contains the tip with title "testTitle"
 
   
   @dev
   Scenario: Tips can be edited
    	Given  a user account with the email "example@example.com" exists
    	And    the user "example@example.com" is logged in
    	And    the database is initialized for tips_can_be_edited 
    	And    the url is "/tips/"
   	
    	When  the user presses the button to edit a tip
		And   enters title "test2", chooses the type "Website", enters description"test2" and enters a webpage "https://www.youtube.com" into the edit form
		And   the edit is submitted
 
    	Then  the page contains a tip with title "test2", type "Website", desc "test2" and url "https://www.youtube.com"
   	
 
