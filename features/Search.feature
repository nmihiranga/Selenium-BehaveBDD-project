Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to the home page
    When I enter a valid product into the search box
    And I press enter key
    Then Valid product should get displayed in search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to the home page
    When I enter a invalid product into the search box
    And I press enter key
    Then product not found message should displayed in search results