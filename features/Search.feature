Feature: Search functionality

  Scenario: Search for a valid product
    Given I got navigated to the home page
    When I enter a valid product into the search box
    And I click on search button
    Then Valid product should get displayed in search results

  Scenario: Search for an invalid product
    Given I got navigated to the home page
    When I enter a invalid product into the search box
    And I click on search button
    Then product not found message should displayed in search results

  Scenario: Search without entering any product
    Given I got navigated to the home page
    When I don't enter anything into the search box
    And I click on search button
    Then product not found message should displayed in search results