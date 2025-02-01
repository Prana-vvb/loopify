# Loopify - Spotify Track Looper

Loopify is a simple Python script that allows you to loop a specific portion of a track while listening on Spotify. It periodically checks the current playback position and resets it to the loop start time when it reaches the loop end time.

## Prerequisites
- A Spotify Premium account (Spotify API requires Premium for playback control).
- A registered Spotify Developer Application. (Because I'm too lazy to deploy this as a website, screw React)

## Installation 

1. **Clone the repository:**
   ```sh
   git clone https://github.com/amateurmonke/loopify.git
   cd loopify
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install spotipy
   ```

4. **Set up Spotify API credentials:**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application.
   - Note down the `Client ID` and `Client Secret`.
   - Set the Redirect URI to: `http://localhost:3000/callback`.

5. **Set up environment variables:**
   
   **MacOS/Linux:**
   Create a `.env` file in the project root and add:
   ```sh
   SPOTIFY_CLIENT_ID="your_client_id_here"
   SPOTIFY_CLIENT_SECRET="your_client_secret_here"
   ```
   Then, run:
   ```sh
   source ~/.zshrc
   ```
   **Windows:**
   ```sh
   setx SPOTIFY_CLIENT_ID "your_client_id"
   setx SPOTIFY_CLIENT_SECRET "your_client_secret"

   ```

## Usage

1. **Run the script:**
   ```sh
   python main.py
   ```

2. **Modify the loop range:**
   - Edit `loop_start` and `loop_end` in `main.py` to set the desired loop section (in seconds).

3. **Ensure Spotify is running:**
   - A track must be playing on a device linked to your Spotify account.
