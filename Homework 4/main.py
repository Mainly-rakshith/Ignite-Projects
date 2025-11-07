# Name: Rakshith Jayakarthikeyan
# Assignment: PROG 1003 - HW4 - GeoPin

from barcode import is_valid_zip, compute_check_digit, make_barcode

def main():
    zip_code = input("Enter zipcode: ").strip()

    if not is_valid_zip(zip_code):
        print("Error: Invalid ZIP code. Must be exactly 5 digits.")
        return

    check = compute_check_digit(zip_code)
    barcode = make_barcode(zip_code, check)

    print(f"The barcode is {barcode}")
    print(f"The zipcode is {zip_code}, Check digit is {check}")

if __name__ == "__main__":
    main()