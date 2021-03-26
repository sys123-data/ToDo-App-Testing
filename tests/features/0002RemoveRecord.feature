Feature Remove record

  Remove record

 Scenario Outline: Remove record
    Given I access the website
    When I remove <value>
    Then <value> should not be available
   Examples:
   |value|
   |abc|

