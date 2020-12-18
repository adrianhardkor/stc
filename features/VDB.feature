Feature: Test Ping Functionality
  @demo @XT-229
  Scenario: PING_EXPECTED_TRUE
    Given Spirent config built
    When I try to ping "10.88.48.32"
    Then I expect response "true"
