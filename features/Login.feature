Feature: Login functionality

  Scenario: Login with valid credentials
    Given I navigated to the login page
    When I enter valid email and valid password into the fields
    And I click on login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    Given I navigated to the login page
    When I enter invalid email and valid password into the fields
    And I click on login button
    Then I should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given I navigated to the login page
    When I enter valid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  Scenario: Login with invalid credentials
    Given I navigated to the login page
    When I enter invalid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  Scenario: Login without entering any credentials
    Given I navigated to the login page
    When I don't enter anything into the fields
    And I click on login button
    Then I should get a proper warning message