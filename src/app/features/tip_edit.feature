Feature: edit a tip

  Scenario: edit via edit button
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    When  the user presses the button to edit a tip
    And   the Website edit form is filled with the title "test2", description "test2" and url "https://www.youtube.com"
    And   the edit form is submitted
    Then  the page contains a tip with title "test2", type "Website", desc "test2" and url "https://www.youtube.com"

  Scenario: invalid edit via edit button
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    When  the user presses the button to edit a tip
    And   the Website edit form is filled with the title "test2", description "test2" and url "invalid input"
    And   the edit form is submitted
    Then  the page contains the text "Update reading tip"