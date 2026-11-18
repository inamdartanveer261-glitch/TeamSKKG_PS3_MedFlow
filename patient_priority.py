def prioritize_patients(patients):
    priority_order = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    return sorted(
        patients,
        key=lambda p: priority_order.get(
            p.get("staff_priority", "low").lower(), 5
        )
    )


if __name__ == "__main__":
    demo_patients = [
        {"name": "Patient A", "staff_priority": "medium"},
        {"name": "Patient B", "staff_priority": "critical"},
        {"name": "Patient C", "staff_priority": "high"}
    ]

    for patient in prioritize_patients(demo_patients):
        print(patient["name"], "-", patient["staff_priority"])
