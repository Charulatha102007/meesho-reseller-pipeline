from growth_engine import mom_growth, is_flagged, validate_feed

def test_engine():
    # Test 1
    g1 = mom_growth(104520.77, 185107.61)
    assert g1 == 77.1
    assert is_flagged(g1) == "flagged"

    # Test 2
    g2 = mom_growth(35542.11, 37559.07)
    assert g2 == 5.67
    assert is_flagged(g2) == "not_flagged"

    # Test 3
    g3 = mom_growth(100000.0, 108000.0)
    assert g3 == 8.0
    assert is_flagged(g3, 8.0) == "escalate_exact_boundary"

    # Test 4
    valid, errors = validate_feed("fixtures/corrupted_feed.csv")
    assert valid == False
    assert len(errors) == 3

    print("All engine tests passed successfully!")

if __name__ == "__main__":
    test_engine()