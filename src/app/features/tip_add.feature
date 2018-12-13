Feature: add a tip

  Scenario: add via creation form
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the url is "/tips/"
    When  the user presses the button to add new reading tip
    And   the Website creation form is filled with the title "test", description "test" and url "https://www.google.fi"
    And   the tip is submitted
    Then  the page contains the added tip with title "test"