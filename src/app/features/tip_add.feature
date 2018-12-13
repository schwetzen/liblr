Feature: add a tip

  Scenario: add via creation form
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the url is "/tips/"
    When  the user presses the button to add new reading tip
    And   enters title "test", selects Website, enters description "test" and enters url "https://www.google.fi"
    And   the tip is submitted
    Then  the page contains the added tip with title "test"