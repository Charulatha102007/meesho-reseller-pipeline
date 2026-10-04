import csv

def mom_growth(previous: float, current: float) -> float:
    return round(((current - previous) / previous) * 100.0, 2)

def is_flagged(mom_pct: float, threshold: float = 8.0) -> str:
    if abs(mom_pct) == threshold:
        return "escalate_exact_boundary"
    elif abs(mom_pct) > threshold:
        return "flagged"
    else:
        return "not_flagged"

def validate_feed(csv_path: str):
    errors = []
    try:
        with open(csv_path, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for line_no, row in enumerate(reader, start=2):
                if len(row) < 4:
                    continue
                month, category, revenue_str, n_orders_str = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()
                
                if not category:
                    errors.append(f"line {line_no}: missing category (month={month})")
                    continue
                
                if not revenue_str:
                    errors.append(f"line {line_no}: missing revenue (category={category})")
                    continue
                
                try:
                    rev = float(revenue_str)
                    if rev < 0:
                        errors.append(f"line {line_no}: negative revenue ({rev}) for category={category}")
                except ValueError:
                    errors.append(f"line {line_no}: revenue not numeric: '{revenue_str}'")
                    
    except Exception as e:
        return False, [str(e)]

    if errors:
        return False, errors
    return True, []