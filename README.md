# nethaji

## Chess Best Move Bot

A Streamlit web application that uses the Stockfish chess engine to analyze chess positions and suggest the best move.

### Features

- Enter any chess position in FEN (Forsyth-Edwards Notation) format
- Get the best move suggestion from Stockfish engine
- User-friendly web interface built with Streamlit

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Install Stockfish chess engine:
   - **Ubuntu/Debian**: `sudo apt-get install stockfish`
   - **macOS**: `brew install stockfish`
   - **Windows**: Download from [stockfishchess.org](https://stockfishchess.org/download/)

### Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Then open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`).

### How to Use

1. Enter a chess position in FEN notation (default is the starting position)
2. Click "Get Best Move" button
3. The app will analyze the position and display the best move

### Example FEN Positions

- Starting position: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
- After 1.e4: `rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1`