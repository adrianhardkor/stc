Feature: Test Ping Functionality
  @demo @XT-153
  Scenario: PING_EXPECTED_FALSE
    Given Spirent config built
    When I try to ping "10.44.0.99"
    Then I expect response "false"
