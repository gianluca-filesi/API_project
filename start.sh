#!/bin/bash
# Start the Streamlit app on a custom port (e.g., $STREAMLIT_PORT)
streamlit run app/main.py --server.port ${STREAMLIT_PORT:-8501} --server.address 0.0.0.0 &

# Start the API server on the port provided by Render
uvicorn app.main_api:app --host 0.0.0.0 --port $PORT

# Wait for all background processes to finish
wait
