Feature: register an account

  Scenario: navigation to register page
    Given user is at home page
    When  user presses register button
    Then  user is redirected to register page

  Scenario: register new account
    Given user is at register page
    When  user fills out and submits the register form
    Then  a new user is registered