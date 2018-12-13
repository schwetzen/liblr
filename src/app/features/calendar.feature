Feature: use calendar

  Scenario: navigation to calendar page
    Given the url is "/"
    And a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    When the user selects the calendar view from the navbar
    Then the page contains a button called "today"
    And the url is "/calendar/"

  Scenario: scheduling tip
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    When  the user presses the button to edit a tip
    And   sets the start and end dates
    And   the Website edit form is filled with the title "test2", description "test2" and url "https://www.youtube.com"
    And   the edit form is submitted
    And   the user selects the calendar view from the navbar
    Then  the page contains the text "test2"