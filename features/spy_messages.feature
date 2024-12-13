Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.
    Scenario: I can successfully encode a secret message
        Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
        When I add "test" to the inputfield "#letters"
        And I select the "1" option for element "#shift-amount"
        And I click on the button "#submit"
        And I pause for 200ms
        Then I expect that element "#decoded_message" contains the text "uftu"
    Scenario: I can successfully decode a secret message
        Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
        When I add "uftu" to the inputfield "#letters"
        And I select the "1" option for element "#decoder-setting"
        And I select the "1" option for element "#shift-amount"
        And I click on the button "#submit"
        And I pause for 200ms
        Then I expect that element "#decoded_message" contains the text "test"