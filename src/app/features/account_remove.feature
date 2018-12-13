Feature: remove an account

  Scenario: user deletes existing account
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    When   the user presses the button to delete the account
    And   the user confirms this decision
    Then  the url is "/"

  Scenario: the account is really removed
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    When  the user presses the button to delete the account
    And   the user confirms this decision
    And   the url is "/login/"
    And   the user fills the login form with the username "example@example.com"
    And   the form is submitted
    Then  the url is "/login/"