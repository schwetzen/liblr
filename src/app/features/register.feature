Feature: register an account

  Scenario: navigation to register page
    Given the url is "/"
    When  user presses register button
    Then  the url is "/register/"

  Scenario: register new account
    Given the url is "/register/"
    When  user fills out and submits the register form
    Then  the url is "/login/"