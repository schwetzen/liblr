Feature: register an account

  Scenario: navigation to register page
    Given the url is "/"
    When  the user presses register button
    Then  the url is "/register/"

  Scenario: register new account
    Given the url is "/register/"
    When  the user fills the register form with the email "example@example.com"
    And   the form is submitted
    Then  the url is "/login/"
    And   a user account with the email "example@example.com" exists

  Scenario: register existing account
    Given a user account with the email "example@example.com" exists
    And   the url is "/register/"
    When  the user fills the register form with the email "example@example.com"
    And   the form is submitted
    Then  the url is "/register/"
