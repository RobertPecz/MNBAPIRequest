from helper.menu import Menu


def main():
    main_menu = Menu()
    # modify the date to start a query from-to
    main_menu.create_excel_data("2025-01-15", "2025-02-16")


if __name__ == "__main__":
    main()
