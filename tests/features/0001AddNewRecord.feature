Feature Add new record

  Add new record

 Scenario Outline: Add new record
    Given I access the website
    When I insert <value>
    And I click add
    Then <value> should be available
   Examples:
   |value|
   |abc|

