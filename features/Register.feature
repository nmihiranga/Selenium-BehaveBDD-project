Feature: Register account functionality

  @register
  Scenario Outline: Register with required fields
    Given I navigate to the register page
    When I enter details into required fields as <firstname> <lastname> <email> <password> <confirm_password>
    And I click on signup button
    Then I should get logged in
    Examples:
      | firstname  | lastname   | email              | password | confirm_password |
      | testOneF   | testOneL   | testonea@one.com   | A111$bbb | A111$bbb         |
      | testTwoF   | testTwoL   | testtwoa@one.com   | A111$bbb | A111$bbb         |
      | testThreeF | testThreeL | testthreea@one.com | A111$bbb | A111$bbb         |

  @register
  Scenario: Register with duplicate email
    Given I navigate to the register page
    When I enter below details into all fields except email
      | firstname | lastname | password | confirm_password |
      | test      | test     | A111$bbb | A111$bbb         |
    And I enter already registered email as testone@one.com into email field
    And I click on signup button
    Then Warning message about existing email should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to the register page
    When I don't enter anything into the fields
    And I click on signup button
    Then Warning message about filling required fields should be displayed