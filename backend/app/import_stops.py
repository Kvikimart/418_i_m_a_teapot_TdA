#so after some time of making the admin page i found out we just need to import a .csv dataset this script should take care of it

import csv
from pathlib import Path
from app import create_app
from app.extensions import db
from app.models import Stops

app = create_app()


def parse_bool(value: str) -> bool:
    return str(value).strip().lower() == "true"


CSV_PATH = Path(__file__).resolve().parents[2] / "Media" / "Stops" / "stops.csv"


with app.app_context():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
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

    db.session.commit()