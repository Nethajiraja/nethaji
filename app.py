import streamlit as st
import chess
import chess.engine

# Change this path if needed (for local testing)
STOCKFISH_PATH = "stockfish"

st.title("♟️ Online Chess Best Move Bot")

fen = st.text_area("Enter FEN Position:", 
                   "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

if st.button("Get Best Move"):
    try:
        board = chess.Board(fen)

        engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        result = engine.analyse(board, chess.engine.Limit(depth=15))
        best_move = result["pv"][0]
        engine.quit()

        st.success(f"Best Move: {best_move}")

    except Exception as e:
        st.error("Invalid FEN or Engine Error")
