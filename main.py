"""
A simple version of the idea — no Notion or CRM connections, just the core
logic: read the leads, clean them up, group duplicates, and flag anything
that needs a human to look at it.

Run it like this:
    python simple_pipeline.py notion-qualified-accounts-w34.csv
"""

import csv
import sys


def clean_website(url):
    # remove https://, www., and anything after the domain
    url = url.lower().strip()
    url = url.replace("https://", "").replace("http://", "")
    url = url.replace("www.", "")
    url = url.split("/")[0]
    return url


def clean_employees(text):
    # make all dashes the same
    return text.replace("–", "-").replace("—", "-")


def needs_review(row):
    reasons = []
    if not row["Work email"].strip():
        reasons.append("no email address")
    notes = row.get("Research notes", "").lower()
    if "previously" in notes or "spring campaign" in notes:
        reasons.append("might already be in the CRM")
    return reasons


def main(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # clean up each row
    for row in rows:
        row["Website"] = clean_website(row["Website"])
        row["Employees"] = clean_employees(row["Employees"])

    # group rows by company, so two contacts at the same company
    # become one company with two people, not two companies
    companies = {}
    for row in rows:
        key = row["Website"] or row["Account"]
        companies.setdefault(key, []).append(row)

    ready = []
    review = []

    for company_key, contacts in companies.items():
        for row in contacts:
            reasons = needs_review(row)
            if reasons:
                review.append((row, reasons))
            else:
                ready.append(row)

    # show what would happen
    print(f"\n{len(ready)} row(s) ready to send to the CRM:\n")
    for company_key, contacts in companies.items():
        contacts_ready = [r for r in contacts if not needs_review(r)]
        if contacts_ready:
            print(f"  {contacts[0]['Account']} ({company_key}) — "
                  f"{len(contacts_ready)} contact(s)")

    print(f"\n{len(review)} row(s) need a person to check first:\n")
    for row, reasons in review:
        print(f"  {row['Account']:20s} {row['Contact']:20s} -> {', '.join(reasons)}")


if __name__ == "__main__":
    main(sys.argv[1])