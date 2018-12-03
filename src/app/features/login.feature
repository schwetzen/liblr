Feature: login with an account

  Scenario: navigation to login page
    Given the user is logged out
    And   the url is "/"
    When  the user presses login button
    Then  the url is "/login/"

  Scenario: login with an existing account
    Given the user is logged out
    And   the url is "/login/"
    And   a user account with the email "example@example.com" exists
    When  the user fills the login form with the username "example@example.com"
    And   the form is submitted
    Then  the url is "/"

  Scenario: login with a non-existing account
    Given the user is logged out
    And   the url is "/login/"
    And   a user account with the email "example@example.com" does not exists
    When  the user fills the login form with the username "example@example.com"
    And   the form is submitted
    Then  the url is "/login/"
