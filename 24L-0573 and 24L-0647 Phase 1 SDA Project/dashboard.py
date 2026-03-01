import matplotlib.pyplot as plt
from collections import defaultdict

def create_dashboard(processed, config):
    if not processed:
        return

    data = processed["filtered_data"]
    values = [r["Value"] for r in data]

    op = config.get("operation")

    # First three options: only print results, no charts
    if op in ["average_region", "average_country", "sum_region"]:
        print("\n===== RESULTS =====")
        print("Region:", config.get("region"))
        print("Country:", config.get("country"))
        print("Year:", config.get("year"))
        print("Operation:", op)
        print("Sum:", processed["sum"])
        print("Average:", processed["average"])
        return

    print("\n===== DASHBOARD =====")
    print("Operation:", op)
    print("Sum:", processed["sum"])
    print("Average:", processed["average"])

    # ---------- Overall Charts ----------
    if op == "chart_overall":
        # Bar chart: total GDP per year
        yearly_totals = defaultdict(float)
        for r in data:
            yearly_totals[r["Year"]] += r["Value"]

        years = sorted(yearly_totals.keys())
        totals = [yearly_totals[y] for y in years]

        plt.figure()
        plt.bar(years, totals)
        plt.title("World GDP per Year (Bar Chart)")
        plt.xlabel("Year")
        plt.ylabel("Total GDP (current US$)")

        # Pie chart: total GDP per country (all years summed)
        country_totals = defaultdict(float)
        for r in data:
            country_totals[r["Country Name"]] += r["Value"]

        countries = list(country_totals.keys())
        totals = list(country_totals.values())

        plt.figure()
        plt.pie(totals, labels=countries, autopct="%1.1f%%")
        plt.title("World GDP by Country (Pie Chart)")

        plt.show()
        return

    # ---------- Other Chart Options ----------
    labels = []
    if op == "chart_region":
        labels = [r["Country Name"] for r in data]
    elif op == "chart_year":
        labels = [r["Country Name"] for r in data]
    elif op == "chart_country":
        labels = [str(r["Year"]) for r in data]
    else:
        labels = [f"{r['Country Name']} ({r['Year']})" for r in data]

    plt.figure()
    plt.bar(labels, values)
    plt.title("GDP Bar Chart")
    plt.xticks(rotation=90)
    plt.ylabel("GDP (current US$)")

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("GDP Pie Chart")

    plt.show()
