import jwt


# SUPPRESSION TEST: this finding is intentionally suppressed via cloak:ignore.
# It should appear in the scan report's suppress.inline count (not as a finding).
# Auditors can see suppressions in the scan detail and code diff.
def decode_test_fixture(token: str) -> dict:
    return jwt.decode(token, options={"verify_signature": False})  # cloak:ignore reason="test fixture — not reachable from any production code path"
