from datetime import datetime
import argparse

CRONTAB_PATH = "/etc/crontab"

def update_crontab_date(iso_date_str, match_string):

    dt = datetime.strptime(iso_date_str, "%Y-%m-%dT%H:%M:%S.000Z")
    minute = dt.minute
    hour = dt.hour
    day = dt.day
    month = dt.month

    updated = False
    new_lines = []

    with open(CRONTAB_PATH, "r") as f:
        lines = f.readlines()

    for line in lines:
        if match_string in line and not line.strip().startswith("#"):
            parts = line.split()
            if len(parts) < 7:
                new_lines.append(line)
                continue

            # Substituir os campos
            old = line.strip()
            parts[0] = str(minute)
            parts[1] = str(hour)
            parts[2] = str(day)
            parts[3] = str(month)
            new_line = " ".join(parts) + "\n"
            print(f"Atualizado:\n  De: {old}\n  Para: {new_line.strip()}")
            new_lines.append(new_line)
            updated = True
        else:
            new_lines.append(line)

    if not updated:
        raise ValueError(f"Nenhuma linha encontrada com: {match_string}")

    with open(CRONTAB_PATH, "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Atualiza uma linha do crontab com nova data.")
    parser.add_argument("iso_date", help="Data em formato ISO ex: 2025-06-11T09:00:00.000Z")
    parser.add_argument("match_string", help="Texto que identifica a linha do crontab a atualizar")

    args = parser.parse_args()

    try:
        update_crontab_date(args.iso_date, args.match_string)
    except Exception as e:
        print(f"Erro: {e}")