Feature: Test Ping Functionality
  @demo @XT-155
  Scenario: PING_EXPECTED_FAIL
    Given Spirent config built
    When I try to ping "10.44.0.99"
    Then I expect response "true"
