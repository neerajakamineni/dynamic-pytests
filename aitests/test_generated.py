
import pytest

# Function to process claims
def process_claim(claim_amount, coverage, documentation):
    """
    Processes a claim based on the provided parameters.
    Returns 'ACCEPTED' if the claim meets all criteria, otherwise 'REJECTED'.
    """
    if claim_amount <= 0:
        return 'REJECTED'
    if not documentation:
        return 'REJECTED'
    if coverage <= 0 or coverage > 1:
        return 'REJECTED'
    return 'ACCEPTED'

# Test data
test_data = [
    # Positive scenario: Valid claim
    (500, 0.8, True, 'ACCEPTED'),
    # Negative scenario: Claim amount is zero
    (0, 0.8, True, 'REJECTED'),
    # Negative scenario: Missing documentation
    (500, 0.8, False, 'REJECTED'),
    # Negative scenario: Invalid coverage (greater than 1)
    (500, 1.2, True, 'REJECTED'),
    # Negative scenario: Invalid coverage (less than or equal to 0)
    (500, 0, True, 'REJECTED'),
]

@pytest.mark.parametrize("claim_amount, coverage, documentation, expected_status", test_data)
def test_process_claim(claim_amount, coverage, documentation, expected_status):
    """
    Test the process_claim function with various inputs.
    """
    result = process_claim(claim_amount, coverage, documentation)
    assert result == expected_status