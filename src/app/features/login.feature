Feature: login with an account

  Scenario: navigation to login page
    Given the url is "/"
    When  the user presses the login button
    Then  the url is "/login/"

  Scenario: login with an existing account
    Given a user account with the email "example@example.com" exists
    And   the url is "/login/"
    When  the user fills the login form with the username "example@example.com"
    And   the form is submitted
    Then  the url is "/"

  Scenario: login with a non-existing account
    Given the url is "/login/"
    When  the user fills the login form with the username "example@example.com"
    And   the form is submitted
    Then  the url is "/login/"
