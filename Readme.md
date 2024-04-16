# Birthday Greeting Automation

This Python script automates the process of sending birthday greetings to employees using Google Sheets as a database and Slack for communication.

## Setup

### 1. Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ubaidmanzoor987/birthday-greeting-automation
   ```

2. Navigate to the project directory:

   ```
   cd birthday-greeting-automation
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

### 2. Set up Google Sheets API

1. Enable the Google Sheets API for your Google Cloud project.

2. Create a service account and download the JSON key file.

3. Rename the JSON key file to `birthday.json` and place it in the project directory.

### 3. Configure Slack Integration

1. Create an incoming webhook for your Slack workspace.

2. Copy the webhook URL.

3. Create a `.env` file in the project directory and add the following lines:

   ```
   COMPANY_NAME=<COMPANY_NAME>
   SLACK_WEBHOOK_URL=<your-slack-webhook-url>
   ```

### 4. Set up Google Sheets

1. Create a Google Sheets spreadsheet with the following columns: `Name`, `DOB` (Date of Birth).

2. Add employee names and their dates of birth to the spreadsheet.

### 5. Run the Script

Execute the Python script by running the following command:

## Usage

The script will automatically check for birthdays in the Google Sheets spreadsheet and send birthday greetings to employees via Slack.
