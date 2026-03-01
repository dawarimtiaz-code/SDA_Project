def process_data(data, config):
    filtered = []

    # Special case: overall charts (no filtering)
    if config.get("operation") == "chart_overall":
        # Collect all values for every country and year
        for row in data:
            for y in range(1960, 2025):
                val = row.get(str(y), "")
                if val:
                    try:
                        filtered.append({
                            "Country Name": row["Country Name"],
                            "Year": y,
                            "Value": float(val)
                        })
                    except:
                        continue
    else:
        # Normal filtering
        for row in data:
            if config.get("region") and row.get("Continent", "").lower() != config["region"].lower():
                continue
            if config.get("country") and row.get("Country Name", "").lower() != config["country"].lower():
                continue

            if config.get("year"):
                value = row.get(str(config["year"]), "")
                if value:
                    try:
                        filtered.append({
                            "Country Name": row["Country Name"],
                            "Year": config["year"],
                            "Value": float(value)
                        })
                    except:
                        continue
            else:
                for y in range(1960, 2025):
                    val = row.get(str(y), "")
                    if val:
                        try:
                            filtered.append({
                                "Country Name": row["Country Name"],
                                "Year": y,
                                "Value": float(val)
                            })
                        except:
                            continue

    if not filtered:
        print("No data after filtering.")
        return None

    values = [r["Value"] for r in filtered]
    total = sum(values)
    avg = total / len(values)

    return {
        "filtered_data": filtered,
        "sum": total,
        "average": avg
    }
