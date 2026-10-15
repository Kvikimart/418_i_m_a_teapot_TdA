#so after some time of making the admin page i found out we just need to import a .csv dataset this script should take care of it

import csv
from pathlib import Path
from app.extensions import db
from app.models import Stops


def parse_bool(value: str) -> bool:
    return str(value).strip().lower() == "true"


# The server image is built with ./backend as the Docker context, so the CSV
# must live inside backend/ to be copied into the container (/app/data).
CSV_CANDIDATES = (
    Path(__file__).resolve().parents[1] / "data" / "stops.csv",
    Path("/app/data/stops.csv"),
)


def resolve_csv_path() -> Path:
    for path in CSV_CANDIDATES:
        if path.exists():
            return path
    candidate_list = ", ".join(str(path) for path in CSV_CANDIDATES)
    raise FileNotFoundError(f"stops.csv not found. Tried: {candidate_list}")


def import_stops_data(csv_path: Path | None = None) -> int:
    csv_path = csv_path or resolve_csv_path()
    imported = 0
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stop = Stops(
                id=int(row["id"]),
                name=row["name"],
                lines=row["lines"],
                is_transfer=parse_bool(row["is_transfer"]),
                transfer_lines=row["transfer_lines"],
                x=row["x"],
                y=row["y"],
                wheelchair_accessible=parse_bool(row["wheelchair_accessible"]),
                has_shelter=parse_bool(row["has_shelter"]),
                has_bench=parse_bool(row["has_bench"]),
                has_ticket_machine=parse_bool(row["has_ticket_machine"]),
                has_display=parse_bool(row["has_display"]),
                image_url=row["image_url"],
            )
            db.session.merge(stop)
            imported += 1

    db.session.commit()
    return imported


if __name__ == "__main__":
    from app import create_app

    app = create_app()
    with app.app_context():
        imported = import_stops_data()
        print(f"Imported {imported} stops")