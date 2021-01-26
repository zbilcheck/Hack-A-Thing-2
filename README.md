# Hack-A-Thing-2
Chloe Son, Bruce Zou, Hershel Wathore, Urie Choi, Zachary Bilcheck

## Description

For this hack-a-thing, we wanted to create a very simple Chrome extension that detects when the user is on Facebook and displays a popup message. The goal was to learn the basics of creating an extension with React and using/integrating serverless functions (AWS Lambda). The extension detects when the user is on Facebook, sends an API request to the AWS Lambda (which just echoes back the name), and displays the alert "Welcome to [name]". [name] is just set to "True Pill".

The extension is contained in the `hackathing2` directory. The API code is in `hackathing2_api`.

## Setup
1. `npm install`
2. `npm run build`
3. Open Chrome and go to `chrome://extensions`
4. Make sure developer mode is on.
5. Click 'Load unpacked'.
6. Browse to the `build` folder of the project and select it.

Api code is included for completeness no setup is needed. An AWS lambda function was created and the code in `api.py` was uploaded there.

## Usage
Navigate to facebook.com and a popup should show up saying "Welcome to True Pill".
