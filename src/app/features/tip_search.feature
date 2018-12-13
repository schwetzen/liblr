Feature: search by keyword

  Scenario: The user can search for tips
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_searched
    When  the user enters the search term "google"
    And   presses the search button
    Then  the user will be presented with tips including keyword "google"
