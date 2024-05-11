Feature: Register account functionality

  Scenario: Register with required fields
    Given I navigate to the register page
    When I enter details into required fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    Given I navigate to the register page
    When I enter details into all fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with duplicate email
    Given I navigate to the register page
    When I enter details into all fields except email
    And I enter already registered email into email field
    And I click on continue button
    Then Warning message about existing email should be displayed

  Scenario: Register without providing any details
    Given I navigate to the register page
    When I don't enter anything into the fields
    And I click on continue button
    Then Warning message about filling required fields should be displayed