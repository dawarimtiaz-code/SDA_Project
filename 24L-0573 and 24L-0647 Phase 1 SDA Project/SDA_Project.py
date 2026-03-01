from data_loader import load_data
from data_processor import process_data
from dashboard import create_dashboard

def main_menu():
    print("\n===== GDP ANALYSIS MENU =====")
    print("1. Average GDP of Regions")
    print("2. Average GDP of a Country")
    print("3. Sum of GDP of Regions")
    print("4. Charts by Country")
    print("5. Charts by Year")
    print("6. Charts by Specific Region")
    print("7. Overall Charts")
    print("8. Exit")

def main():
    data = load_data("data.csv")

    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        config = {
            "region": "",
            "year": "",
            "country": "",
            "operation": ""
        }

        if choice == "1":
            config["region"] = input("Enter Region: ").strip()
            config["operation"] = "average_region"

        elif choice == "2":
            config["country"] = input("Enter Country: ").strip()
            config["operation"] = "average_country"

        elif choice == "3":
            config["region"] = input("Enter Region: ").strip()
            config["operation"] = "sum_region"

        elif choice == "4":
            config["country"] = input("Enter Country: ").strip()
            config["operation"] = "chart_country"

        elif choice == "5":
            config["year"] = input("Enter Year: ").strip()
            config["operation"] = "chart_year"

        elif choice == "6":
            config["region"] = input("Enter Region: ").strip()
            config["operation"] = "chart_region"

        elif choice == "7":
            config["operation"] = "chart_overall"

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")
            continue

        processed = process_data(data, config)
        create_dashboard(processed, config)

if __name__ == "__main__":
    main()
