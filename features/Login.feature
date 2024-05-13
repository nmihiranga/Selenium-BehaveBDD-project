Feature: Login functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to the login page
    When I enter valid <email> and valid <password> into the fields
    And I click on login button
    Then I should get logged in
    Examples:
      | email             | password |
      | testone@one.com   | A111$bbb |
      | testtwo@one.com   | A111$bbb |
      | testthree@one.com | A111$bbb |

  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to the login page
    When I enter invalid email as test@invalid.com and valid password as A111$bbb into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to the login page
    When I enter valid email as testone@one.com and invalid password as invalid into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to the login page
    When I enter invalid email as test@invalid.com and invalid password as invalid into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to the login page
    When I don't enter anything into the fields
    And I click on login button
    Then I should get a warning message to fill required fields