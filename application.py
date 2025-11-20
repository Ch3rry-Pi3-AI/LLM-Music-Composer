"""
Streamlit Interface for the LLMOps Music Composer

This module defines a Streamlit-based web interface for interacting with
the LLM-powered music composition engine.

High-level behaviour:
1. The user describes the kind of music they want (text input).
2. The user selects a target style (e.g. "Jazz", "Sad", "Romantic").
3. The app uses the `MusicLLM` class to:
   - generate a melody from the text description,
   - generate harmony chords for that melody,
   - generate a rhythm pattern for the melody,
   - adapt the overall composition to the requested style.
4. The melodic and harmonic notes are converted to frequencies using
   helper functions from `app.utils`.
5. The frequencies are synthesised into a WAV audio clip, which is
   played directly in the browser via Streamlit's audio widget.
6. A text summary of the composition is shown in an expandable section.

Only the visual presentation and layout of the interface have been
adjusted for aesthetics; the fundamental composition logic is unchanged.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

# Streamlit for building the web UI
import streamlit as st

# LLM-based music generator (melody, harmony, rhythm, style adaptation)
from app.main import MusicLLM

# Audio helper functions (note → frequency, WAV synthesis)
from app.utils import *

# For wrapping raw audio bytes into a file-like object for Streamlit
from io import BytesIO

# To load environment variables (e.g. GROQ_API_KEY) from a .env file
from dotenv import load_dotenv


# ------------------------------------------------------------
# Environment setup
# ------------------------------------------------------------

# Load variables from the .env file into the environment
load_dotenv()


# ------------------------------------------------------------
# Page configuration and header layout
# ------------------------------------------------------------

# Configure the Streamlit page (title, layout, and optional icon)
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎶",
    layout="centered"
)

# Main title at the top of the page
st.title("🎶 AI Music Composer")

# Short description under the title to guide the user
st.markdown(
    "Compose **AI-generated music** by describing the mood, style, or scene. "
    "The app will create a melody, harmony, rhythm, and a styled composition summary."
)

# Provide additional guidance on the sidebar for better UX
with st.sidebar:
    # Sidebar title
    st.header("🎼 How to Use")
    # Simple step-by-step instructions
    st.markdown(
        "1. Enter a short description of the music you want.\n"
        "2. Choose a style from the dropdown.\n"
        "3. Click **Generate Music**.\n\n"
        "You will hear a generated audio clip and see a text summary of the composition."
    )
    # Small note about the underlying technology
    st.caption(
        "Powered by a Groq-hosted LLaMA model and custom audio synthesis utilities."
    )


# ------------------------------------------------------------
# Main input area (description + style selection)
# ------------------------------------------------------------

# Use a container to group the core controls visually
with st.container():
    # Create two columns: left for text input, right for style selection
    col_left, col_right = st.columns([3, 2])

    # Left column: free-text musical description input
    with col_left:
        # Single-line text input where the user describes the desired music
        music_input = st.text_input(
            "Describe the music you want to compose",
            placeholder="E.g. a calm, melancholic piano piece with gentle motion"
        )

    # Right column: style selection dropdown
    with col_right:
        # Dropdown menu for choosing a stylistic direction
        style = st.selectbox(
            "Choose a style",
            ["Sad", "Happy", "Jazz", "Romantic", "Extreme"]
        )

    # Display an informational box under the inputs to set expectations
    st.info(
        "Once you click **Generate Music**, the system will create a melody, "
        "add harmony, suggest a rhythm, and blend them into the chosen style."
    )


# ------------------------------------------------------------
# Single button to trigger music generation
# ------------------------------------------------------------

# A single button; its return value is True only when clicked
generate_clicked = st.button("🎛️ Generate Music")

# If the button is clicked, decide what to do based on whether input is present
if generate_clicked:
    # If the user has not entered any description, show a warning instead of running the pipeline
    if not music_input:
        st.warning("Please describe the music you want to compose before generating.")

    else:
        # Create an instance of the LLM-based music generator
        generator = MusicLLM()

        # Show a spinner while the model and synthesis work is happening
        with st.spinner("Composing your music..."):
            # --------------------------------------------------------
            # Step 1: Generate a melody from the user description
            # --------------------------------------------------------
            # The model returns a space-separated string of note labels
            melody = generator.generate_melody(music_input)

            # --------------------------------------------------------
            # Step 2: Generate harmony chords for the melody
            # --------------------------------------------------------
            # The model returns chords in a format such as "C4-E4-G4 F4-A4-C5"
            harmony = generator.generate_harmony(melody)

            # --------------------------------------------------------
            # Step 3: Generate rhythm durations for the melody
            # --------------------------------------------------------
            # The model returns beat durations such as "1.0 0.5 0.5 2.0"
            rhythm = generator.generate_rythm(melody)

            # --------------------------------------------------------
            # Step 4: Adapt the combined musical material to the chosen style
            # --------------------------------------------------------
            # The model returns a single-string description of the styled composition
            composition = generator.adapt_style(style, melody, harmony, rhythm)

            # --------------------------------------------------------
            # Step 5: Convert melody notes to frequencies
            # --------------------------------------------------------

            # Break the melody string into individual note tokens
            melody_notes = melody.split()

            # Convert each note label into its corresponding frequency in Hz
            melody_freqs = note_to_frequencies(melody_notes)

            # --------------------------------------------------------
            # Step 6: Convert harmony chords to frequencies
            # --------------------------------------------------------

            # Split the harmony string into chord tokens (e.g. "C4-E4-G4")
            harmony_chords = harmony.split()

            # Prepare an empty list to store all individual harmony notes
            harmony_notes = []

            # For each chord, split it into separate notes by the '-' separator
            for chord in harmony_chords:
                harmony_notes.extend(chord.split("-"))

            # Convert each harmony note label into a frequency in Hz
            harmony_freqs = note_to_frequencies(harmony_notes)

            # --------------------------------------------------------
            # Step 7: Combine melody and harmony frequencies
            # --------------------------------------------------------

            # Concatenate the melody and harmony frequencies into one sequence
            all_freqs = melody_freqs + harmony_freqs

            # --------------------------------------------------------
            # Step 8: Generate a WAV file from the combined frequencies
            # --------------------------------------------------------

            # Use the utility function to synthesise a WAV byte sequence
            wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)

        # ------------------------------------------------------------
        # Audio playback and composition summary display
        # ------------------------------------------------------------

        # Play the generated audio clip inside the app
        st.audio(BytesIO(wav_bytes), format="audio/wav")

        # Notify the user that the process has completed successfully
        st.success("✅ Music generated successfully!")

        # Show the LLM's styled composition summary in an expandable panel
        with st.expander("📝 Composition Summary"):
            # Display the textual description returned by the model
            st.text(composition)
