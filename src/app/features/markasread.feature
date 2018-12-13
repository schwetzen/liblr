Feature: mark reading tips as reading

  Scenario: marking reading tip as read
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    And   a tip is marked as read
    Then  Then the page contains the text "Mark as unread"

  Scenario: NOT marking reading tip as read
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    Then  Then the page does not contain the text "Mark as unread"

  Scenario: marking reading tip as unread
    Given a user account with the email "example@example.com" exists
    And   the user "example@example.com" is logged in
    And   the database is initialized for tips_can_be_edited
    And   the url is "/tips/"
    And   a tip is marked as read
    And   a tip is marked as unread
    Then  Then the page does not contain the text "Mark as unread"