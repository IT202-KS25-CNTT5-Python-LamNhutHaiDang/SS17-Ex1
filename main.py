current_playlist = []

def process_song_data():
    song_title = input("Nhập tên bài hát: ").strip()
    artist_name = input("Nhập tên nghệ sĩ: ").strip()

    if song_title == "" or artist_name == "":
        print("\nTên bài hát và Nghệ sĩ không được để trống.")
        return None

    genres_string = input(
        "Nhập danh sách thể loại, cách nhau bởi dấu phẩy: "
    )

    song_title = song_title.title()
    artist_name = artist_name.upper()

    genre_list = genres_string.split(",")

    genre_list = [genre.strip() for genre in genre_list]

    print("\nThông tin bài hát sau khi chuẩn hóa:")
    print("Tên bài hát:", song_title)
    print("Nghệ sĩ:", artist_name)
    print("Danh sách thể loại:", genre_list)
    print("Số lượng thể loại:", len(genre_list))

    return f"{song_title} - {artist_name}"


def display_playlist():
    print("\n--- PLAYLIST HIỆN TẠI ---")

    if len(current_playlist) == 0:
        print("Playlist hiện đang trống.")
        return

    for index, song in enumerate(current_playlist, start=1):
        print(f"{index}. {song}")

    print("-------------------------")
    print(f"Tổng số bài hát hiện có: {len(current_playlist)}")

def add_song():
    print("\n--- THÊM BÀI HÁT MỚI ---")

    song_info = process_song_data()

    if song_info is None:
        return

    current_playlist.append(song_info)

    print(f"\nĐã thêm bài hát vào Playlist: {song_info}")

def insert_song():
    print("\n--- CHÈN BÀI HÁT VÀO PLAYLIST ---")

    index_input = input("Nhập vị trí index muốn chèn: ")

    if not index_input.isdigit():
        print("Lựa chọn phải là số nguyên, vui lòng nhập lại.")
        return

    insert_index = int(index_input)

    song_info = process_song_data()

    if song_info is None:
        return

    if insert_index < 0 or insert_index > len(current_playlist):

        print("\nVị trí chèn không hợp lệ.")
        print("Bài hát sẽ được thêm vào cuối Playlist.")

        current_playlist.append(song_info)

        print(f"\nĐã thêm bài hát vào cuối Playlist: {song_info}")

    else:

        current_playlist.insert(insert_index, song_info)

        print(
            f"\nĐã chèn bài hát vào vị trí index "
            f"{insert_index}: {song_info}"
        )

def remove_song():
    print("\n--- XÓA BÀI HÁT THEO TÊN ---")

    song_name = input(
        "Nhập chính xác tên bài hát cần xóa: "
    ).strip()

    if song_name in current_playlist:

        current_playlist.remove(song_name)

        print(
            f"\nĐã xóa bài hát khỏi Playlist: "
            f"{song_name}"
        )

    else:

        print("\nBài hát không tồn tại trong Playlist.")

def pop_song():
    if len(current_playlist) == 0:
        print(
            "Playlist hiện đang trống, "
            "vui lòng thêm bài hát trước (Chức năng 1)."
        )
        return

    print("\n--- XÓA BÀI HÁT CUỐI CÙNG ---")

    removed_song = current_playlist.pop()

    print(f"Đã xóa bài hát cuối cùng: {removed_song}")

def search_and_replace():
    if len(current_playlist) == 0:
        print(
            "Playlist hiện đang trống, "
            "vui lòng thêm bài hát trước (Chức năng 1)."
        )
        return

    print("\n--- TÌM KIẾM VÀ THAY THẾ TÊN BÀI HÁT ---")

    search_keyword = input(
        "Nhập từ khóa cần tìm: "
    ).strip()

    replace_keyword = input(
        "Nhập từ khóa thay thế: "
    ).strip()

    changed_count = 0

    print("\nCác bài hát đã được thay đổi:")

    for index in range(len(current_playlist)):

        old_song = current_playlist[index]

        if search_keyword.lower() in old_song.lower():

            new_song = old_song.replace(
                search_keyword,
                replace_keyword
            )

            if old_song.lower() != new_song.lower():

                current_playlist[index] = new_song

                changed_count += 1

                print(
                    f"{changed_count}. "
                    f"{old_song} -> {new_song}"
                )

    if changed_count == 0:

        print(
            "Không tìm thấy bài hát nào "
            "chứa từ khóa này."
        )

    else:

        print(
            f"\nTổng số lần thay thế thành công: "
            f"{changed_count}"
        )

def sort_playlist():

    if len(current_playlist) == 0:
        print(
            "Playlist hiện đang trống, "
            "vui lòng thêm bài hát trước (Chức năng 1)."
        )
        return

    print("\n--- SẮP XẾP DANH SÁCH PHÁT ---")
    print("1. Sắp xếp A-Z")
    print("2. Đảo ngược danh sách")

    choice = input("Chọn kiểu sắp xếp: ").strip()

    if choice == "1":

        current_playlist.sort()

        print(
            "\nĐã sắp xếp Playlist theo "
            "thứ tự A-Z."
        )

    elif choice == "2":

        current_playlist.reverse()

        print(
            "\nĐã đảo ngược thứ tự Playlist."
        )

    else:

        print(
            "Lựa chọn phải là số nguyên, "
            "vui lòng nhập lại."
        )
        return

    display_playlist()

def playlist_management_menu():

    while True:

        print("\n========== QUẢN LÝ DANH SÁCH PHÁT ==========")
        print("1. Chèn bài hát vào vị trí bất kỳ")
        print("2. Xóa bài hát theo tên chính xác")
        print("3. Xóa bài hát cuối cùng")
        print("4. Xem Playlist")
        print("5. Quay lại menu chính")
        print("============================================")

        choice = input(
            "Chọn chức năng con (1-5): "
        ).strip()

        if choice == "1":
            insert_song()

        elif choice == "2":
            remove_song()

        elif choice == "3":
            pop_song()

        elif choice == "4":
            display_playlist()

        elif choice == "5":
            break

        else:
            print(
                "Lựa chọn phải là số nguyên, "
                "vui lòng nhập lại."
            )

while True:

    print("\n========== HỆ THỐNG QUẢN LÝ PLAYLIST SPOTIFY ==========")
    print("1. Thêm bài hát mới & Phân tích dữ liệu")
    print("2. Quản lý danh sách phát")
    print("3. Tìm kiếm và thay thế tên bài hát")
    print("4. Sắp xếp danh sách phát")
    print("5. Thoát chương trình")
    print("=======================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        add_song()

    elif choice == "2":
        playlist_management_menu()

    elif choice == "3":
        search_and_replace()

    elif choice == "4":
        sort_playlist()

    elif choice == "5":
        print(
            "\nDữ liệu Playlist đã được lưu. "
            "Đóng hệ thống Spotify Curation."
        )
        break

    else:
        print(
            "Lựa chọn phải là số nguyên, "
            "vui lòng nhập lại."
        )