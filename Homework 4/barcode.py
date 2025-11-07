ENCODE_TABLE = {
    0: [1, 1, 0, 0, 0],
    1: [0, 0, 0, 1, 1],
    2: [0, 0, 1, 0, 1],
    3: [0, 0, 1, 1, 0],
    4: [0, 1, 0, 0, 1],
    5: [0, 1, 0, 1, 0],
    6: [0, 1, 1, 0, 0],
    7: [1, 0, 0, 0, 1],
    8: [1, 0, 0, 1, 0],
    9: [1, 0, 1, 0, 0],
}

def is_valid_zip(zip_code: str) -> bool:
    return len(zip_code) == 5 and zip_code.isdigit()

def compute_check_digit(zip_code: str) -> int:
    total = sum(int(d) for d in zip_code)
    return (10 - (total % 10)) % 10

def digit_to_barcode(digit: int) -> str:
    pattern = ENCODE_TABLE[digit]
    return "".join("|" if bit == 1 else ":" for bit in pattern)

def make_barcode(zip_code: str, check_digit: int) -> str:
    full_code = [int(d) for d in zip_code] + [check_digit]
    bars = "".join(digit_to_barcode(d) for d in full_code)
    return f"|{bars}|"