# Rain Alert Python Script

This Python script fetches weather data using an API and sends an email alert if rain is expected.

## Prerequisites

Before running the script, ensure you have the following:
- Python installed
- `requests`, `smtplib`, and `dotenv` modules
- An email account for sending alerts
- API key for a weather service

## Installation

1. Clone this repository or copy the script.
2. Install dependencies using:
   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project directory and add the following environment variables:
   ```ini
   my_email=your_email@example.com
   mypassword=your_email_password
   api_key=your_weather_api_key
   weather_url=https://api.openweathermap.org/data/2.5/forecast
   ```

## Usage

Run the script using:
```bash
python script.py
```

## How It Works

1. Loads environment variables from `.env`.
2. Fetches weather forecast data.
3. Checks if rain is expected in the next 4 forecast periods.
4. Sends an email alert if rain is predicted.

## Environment Variables

Environment variables are used to store sensitive data securely. To set them:
```bash
export my_email=your_email@example.com
export mypassword=your_email_password
export api_key=your_weather_api_key
export weather_url=https://api.openweathermap.org/data/2.5/forecast
```

## Notes

- Ensure your email provider allows SMTP access.
- Use an app-specific password if required.
- Modify latitude and longitude values as needed.


