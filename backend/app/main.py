from app.config.settings import settings


def main() -> None:
    """Entry point for the CareerOS backend application.

    Initializes the system by parsing configurations and displaying server status.
    """
    print("CareerOS Backend Service Initializing...")
    print(f"Active Environment: {settings.env}")

    # Access database settings and mask the password for security in logs
    db_settings = settings.db
    masked_url = db_settings.url.replace(db_settings.password, "********")

    print(f"Database Target: {db_settings.host}:{db_settings.port}/{db_settings.db}")
    print(f"Connection URL (Masked): {masked_url}")
    print("CareerOS Backend Service Initialized Successfully.")


if __name__ == "__main__":
    main()
