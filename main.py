raw_logs = []
processed_logs = []


def clean_logs(input_text):
    """
    Làm sạch log bằng translate + split
    """
    table = str.maketrans("", "", "!@#$")
    cleaned = input_text.translate(table)
    return [log.strip() for log in cleaned.split(";") if log.strip()]


def filter_logs(logs):
    """
    Lọc ERROR / CRITICAL bằng list comprehension
    """
    return [
        log for log in logs
        if "error" in log.lower() or "critical" in log.lower()
    ]


def mask_ip(log):
    """
    Che IP dạng xxx.xxx.xxx.xxx -> xxx.xxx.*.*
    """
    words = log.split()

    for i in range(len(words)):
        if "." in words[i]:
            parts = words[i].split(".")
            if len(parts) == 4 and all(p.isdigit() for p in parts):
                words[i] = f"{parts[0]}.{parts[1]}.*.*"

    return " ".join(words)


def mask_ip_logs(logs):
    """
    Áp dụng mask IP cho toàn bộ logs
    """
    return [mask_ip(log) for log in logs]


def input_logs():
    """
    Nhập và làm sạch log
    """
    global raw_logs

    print("\n--- NAP DU LIEU LOG ---")
    data = input("Nhap log thô: ")

    raw_logs = clean_logs(data)

    print(f"Da lam sach va luu {len(raw_logs)} dong log.")


def filter_error_logs():
    """
    Lọc log cảnh báo
    """
    global processed_logs

    if not raw_logs:
        print("Chua co du lieu log, vui long thuc hien chuc nang 1")
        return

    processed_logs = filter_logs(raw_logs)

    if not processed_logs:
        print("Khong tim thay canh bao nguy hiem")
        return

    print("\n--- LOC CANH BAO ---")
    print(f"Tim thay {len(processed_logs)} canh bao nguy hiem:")
    for log in processed_logs:
        print("-", log)


def mask_logs():
    """
    Mã hóa IP trong logs
    """
    if not processed_logs:
        print("Chua co du lieu log, vui long thuc hien chuc nang 2")
        return

    masked = mask_ip_logs(processed_logs)

    print("\n--- MA HOA IP ---")
    print("Bao cao log an toan:")

    for i, log in enumerate(masked, 1):
        print(f"{i}. {log}")


def main():
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhap va lam sach log")
        print("2. Loc log canh bao")
        print("3. Ma hoa IP")
        print("4. Thoat")
        print("==================================================")

        choice = input("Chon (1-4): ").strip()

        match choice:
            case "1":
                input_logs()
            case "2":
                filter_error_logs()
            case "3":
                mask_logs()
            case "4":
                print("He thong da dong. Tam biet!")
                break
            case _:
                print("Lua chon khong hop le!")


main()