def print_report(mismatches):
    if not mismatches:
        print("✅ Design matches production.")
    else:
        print("❌ Mismatches found:")
        for issue in mismatches:
            print(f" - {issue}")
