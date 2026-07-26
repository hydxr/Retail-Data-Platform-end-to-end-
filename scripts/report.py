import os

def generate_reports(summary):
    os.makedirs("reprots",exist_ok=True)
    report_path = "reports/etl_summary.txt"

    with open(report_path,"w") as file:
        file.write("=" * 40 + "\n")
        file.write("        ETL SUMMARY REPORT\n")
        file.write("=" * 40 + "\n\n")

        for key, value in summary.items():
            file.write(f"{key:<30}: {value}\n")

        file.write("\n")
        file.write("=" * 40)

    return report_path
