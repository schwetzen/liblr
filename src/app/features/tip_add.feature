Feature: add a tip

  Scenario: add website
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the url is "/tips/"
    When  the user presses the button to add new reading tip
    And   the Website creation form is filled with the title "test", description "test" and url "https://www.google.fi"
    And   the tip is submitted
    Then  the page contains the added tip with title "test"
  
  Scenario: add book
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the url is "/tips/"
    When  the user presses the button to add new reading tip
    And   the Book creation form is filled with the title "Introduction to algorithms", description "Useful course material" and isbn "978-0-262-53305-8"
    And   the tip is submitted
    Then  the page contains the added tip with title "Introduction to algorithms"

  Scenario: add website with invalid url
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the url is "/tips/"
    When  the user presses the button to add new reading tip
    And   the Website creation form is filled with the title "test", description "test" and url "this is not a url"
    And   the tip is submitted
    Then  the url is "/tips/create/"