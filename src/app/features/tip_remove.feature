Feature: remove a tip

  Scenario: remove a tip via delete button
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_removed
    And   the url is "/tips/"
    When  the delete button is pressed
    Then  the page no longer contains the tip with title "testTitle"