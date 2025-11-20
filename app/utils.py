"""
Music-to-Audio Utilities for LLMOps Music Composer.

This module provides small helper functions for:

1. Converting a list of musical note names (e.g. ["C4", "E4", "G4"])
   into their corresponding frequencies in Hz using `music21`.

2. Generating a WAV audio byte stream from a sequence of frequencies
   by synthesising simple sine waves for each frequency using the
   `synthesizer` package.

The generated WAV bytes can be:
- written directly to a file,
- streamed to a browser,
- or returned as a response from a web API endpoint.
"""

import io  # In-memory byte buffer for WAV data

import music21  # Music theory toolkit (notes, pitches, frequencies)
import numpy as np  # Numerical operations (array handling)
from scipy.io.wavfile import write as write_wav  # WAV writer
from synthesizer import Synthesizer, Waveform  # Simple audio synthesiser


# ------------------------------------------------------------------
# Convert note names (e.g. "C4", "A3") to their frequencies in Hz
# ------------------------------------------------------------------
def note_to_frequencies(note_list):
    """
    Convert a list of musical note names into a list of frequencies in Hz.

    Parameters
    ----------
    note_list : list of str
        List of note names in standard music notation
        (e.g. ["C4", "E4", "G4", "A3"]).

    Returns
    -------
    list of float
        List of frequencies in Hz corresponding to valid notes.
        Any notes that cannot be parsed are silently skipped.
    """
    # Create an empty list to store the resulting frequencies
    freqs = []

    # Loop over every note name provided by the caller
    for note_str in note_list:
        try:
            # Create a `music21` Note object from the string label
            note = music21.note.Note(note_str)

            # Append the frequency (in Hz) of the note's pitch
            freqs.append(note.pitch.frequency)
        except Exception:
            # Ignore any note strings that cannot be parsed
            # (e.g. invalid spelling or malformed input)
            continue

    # Return the list of successfully converted frequencies
    return freqs


# ------------------------------------------------------------------
# Generate a WAV byte stream from a list of frequencies
# ------------------------------------------------------------------
def generate_wav_bytes_from_notes_freq(notes_freq):
    """
    Synthesis a short WAV clip from a sequence of note frequencies.

    For each frequency in `notes_freq`, this function generates
    a 0.5 second sine wave and concatenates them into a single
    audio clip. The result is returned as raw WAV bytes.

    Parameters
    ----------
    notes_freq : list of float
        Frequencies in Hz to be synthesised into audio.

    Returns
    -------
    bytes
        The complete WAV file contents as a bytes object.
    """
    # Create a simple synthesiser that uses a single sine-wave oscillator
    synth = Synthesizer(
        osc1_waveform=Waveform.sine,  # Use a pure sine wave
        osc1_volume=1.0,              # Full volume for oscillator 1
        use_osc2=False                # Disable the second oscillator
    )

    # Define the audio sample rate (44.1 kHz is CD quality)
    sample_rate = 44100

    # Generate a 0.5 second wave for each frequency and join them together
    # into a single 1D NumPy array
    audio = np.concatenate(
        [synth.generate_constant_wave(freq, 0.5) for freq in notes_freq]
    )

    # Create an in-memory bytes buffer to hold the WAV data
    buffer = io.BytesIO()

    # Write the audio array into the buffer as a WAV file
    # - sample_rate defines the sampling frequency
    # - audio is cast to float32 for compatibility with the writer
    write_wav(buffer, sample_rate, audio.astype(np.float32))

    # Return the raw bytes of the generated WAV file
    return buffer.getvalue()
