def alias_for(reseller_id: str) -> str:
    num = reseller_id.replace("RS", "")
    return f"ALIAS-{num}"

def assert_no_raw_names_leak(text: str, reseller_names: list[str]) -> bool:
    for name in reseller_names:
        if name in text:
            return False
    return True