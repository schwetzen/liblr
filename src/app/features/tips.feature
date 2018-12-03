Feature: Tips listing

	Scenario: Tips can be added
		Given  a user account with the email "example@example.com" exists
		And    the user "example@example.com" is logged in

		When   the user presses the button to add new reading tip
		And    enters title "test", chooses the type "website", enters description"test" and enters a webpage "https://www.google.fi"

		Then   the url is "/tips"
		And	   the page contains the new tip


	Scenario: Tips can be removed
		Given  a user account with the email "example@example.com" exists
		And    the user "example@example.com" is logged in

		When   the delete button is pressed
		Then   the page no longer contains the tip data


	Scenario: Tips can be edited
		Given  a user account with the email "example@example.com" exists
		And    the user "example@example.com" is logged in
		
		When   the user presses the button to edit a tip
		And    enters title "test2", chooses the type "website", enters description "test2" and enters a webpage "https://www.youtube.com"

		Then   the url is "/tips"
		And    the page contains the edited tip

		

