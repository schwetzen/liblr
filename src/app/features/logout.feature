Feature: logout with an account

  Scenario: normal logout
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    When  the user presses the logout button
    Then  the url is "/"
    And   the page contains the login link
