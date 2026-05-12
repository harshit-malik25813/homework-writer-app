# Homework Writer App

Homework Writer App is a small Flask project for quickly turning messy homework notes into a clean, consistent format that is easy to copy and send, especially in WhatsApp chats. The goal is simple: reduce repetitive typing and make homework updates look neat without spending extra time formatting each subject by hand.

## What It Does

The app gives you a form for the main school subjects:

- Maths
- Physics
- Chemistry
- Biology
- SST
- Hindi
- English
- Additional notes

After you fill in the subjects you need and submit the form, the app sends the data to `/generate`, formats each subject through helper functions, and then shows the final result on `/output` inside a code block. This makes the output easy to read and easy to copy.

## Inspiration

This project was built from the everyday problem of typing homework boilerplate again and again for WhatsApp. When homework updates need to be sent often, the repeated pattern becomes annoying:

- subject name
- homework text
- date
- extra notes

The app streamlines that process by turning a simple form into a ready-to-send homework message. Instead of retyping the same structure every day, you just enter the subject work once and let the app format it for you.

## How It Works

The flow is intentionally simple:

1. Open the homepage at `/`.
2. Fill in any homework fields you want.
3. Submit the form.
4. The form posts to `/generate`.
5. `app.py` calls the helper functions in `helpers.py`.
6. Each helper returns a formatted line such as `*Maths*: Exercise 4`.
7. The lines are combined into one text block.
8. The app redirects to `/output`.
9. The output page displays the final text inside a code block.

## Project Structure

- `app.py` contains the Flask routes and the function that builds the final homework text.
- `helpers.py` contains the subject formatting helpers and the date helper.
- `templates/index.html` contains the homework form.
- `templates/output.html` displays the generated result.

## Setup

### Requirements

- Python 3.10 or newer
- Flask

### Install Dependencies

If Flask is not installed yet, install it with:

```powershell
pip install flask
```

If you prefer using a virtual environment, create and activate one first, then install Flask inside it.

### Windows Setup

1. Open PowerShell in the project folder.
2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install Flask:

```powershell
pip install flask
```

5. Run the app:

```powershell
flask --app app run --debug
```

### macOS Setup

1. Open Terminal in the project folder.
2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate it:

```bash
source .venv/bin/activate
```

4. Install Flask:

```bash
pip install flask
```

5. Run the app:

```bash
flask --app app run --debug
```

### Linux Setup

1. Open your terminal in the project folder.
2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate it:

```bash
source .venv/bin/activate
```

4. Install Flask:

```bash
pip install flask
```

5. Run the app:

```bash
flask --app app run --debug
```

### Run the App

This project does not need a special build step. Start it with Flask directly:

```powershell
flask --app app run
```

If you want debug mode while developing, use:

```powershell
flask --app app run --debug
```

Then open the local address shown in the terminal, usually `http://127.0.0.1:5000/`.

## Usage

1. Enter homework for any subjects you want.
2. Leave fields blank for subjects that do not need homework.
3. Add anything extra in the Additional field.
4. Submit the form.
5. Copy the generated output from the output page and paste it into WhatsApp or wherever you need it.

## Output Format

The helper functions use a simple markdown-like style so the message looks consistent and easy to scan:

```text
*Maths*: Exercise 4
*Physics*: Read chapter 5
*English*: Summary writing
*12/05/26*
```

That style is intentionally compact because it is meant for fast messaging rather than long document formatting.

## Improvements Over the Older Project

Compared with the earlier version of this project, this version is more complete and easier to use.

### 1. Clearer request flow

The older version mainly rendered the homepage, but this version now has a proper submit flow:

- `/` shows the input form
- `/generate` processes the data
- `/output` shows the formatted result

### 2. Better separation of responsibilities

The logic is now split more cleanly:

- the form lives in the template
- formatting lives in helper functions
- route handling lives in `app.py`

That makes the code easier to explain, test, and change later.

### 3. Safer helper functions

The earlier helper file had a few functions that could fail when a field was empty. Those helpers were cleaned up so every subject formatter now returns a valid string even when no homework is entered.

### 4. Better output presentation

The older version did not have a dedicated result page. This version adds `/output` and shows the final homework inside a code block, which makes it easier to copy without losing line breaks.

### 5. More polished user interface

The form and output pages are styled to feel more like a proper tool and less like a blank demo page. The layout is cleaner, the spacing is more readable, and the page adapts better on smaller screens.

### 6. Easier to teach and explain

Comments were added so the project can be explained step by step, even to beginners. That makes it better for learning Flask and for showing how a basic web app moves data from a form into formatted output.

## Notes

- The current implementation stores the generated homework in memory, so it is best for local use and simple practice projects.
- If you refresh the app or restart the server, the saved output will be cleared.
- A future version could store submissions in a database or generate downloadable text files.

## Possible Future Improvements

- Add persistent storage so output is not lost after restart.
- Let the user choose different output styles.
- Add a copy-to-clipboard button on the output page.
- Add validation so empty submissions are handled more explicitly.
- Support exporting directly to a WhatsApp-ready message format.

## Why This Project Exists

This project exists to save time and remove repetition. Homework messages are usually small, but typing the same structure over and over is still tedious. By turning that routine into a simple form, the app helps produce clean homework text faster and with less effort.
