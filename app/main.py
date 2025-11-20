"""
LLM-Based Music Generation Module

This module defines the `MusicLLM` class, which provides high-level interfaces
for generating musical material using a Groq-hosted LLaMA 3.1 model via LangChain.

The class supports:
1. Melody generation
2. Harmony generation for a melody
3. Rhythm suggestion for a melody
4. Style adaptation combining melody, harmony, and rhythm

Each method uses a dedicated prompt template and executes it through an
LLM chain built with LangChain’s prompt → model pipeline.
"""

import os  # Access environment variables for the Groq API key
from langchain_core.prompts import ChatPromptTemplate  # Prompt templates for structured inputs
from langchain_groq import ChatGroq  # Groq LLM wrapper for LangChain


class MusicLLM:
    """
    A high-level interface for generating musical structures using LLaMA 3.1 through Groq.

    Parameters
    ----------
    temperature : float
        Controls output randomness. Higher values produce more creative results.

    Attributes
    ----------
    llm : ChatGroq
        The Groq LLM client used for all musical generation tasks.
    """

    def __init__(self, temperature=0.7):
        # Initialise the LLM client with a chosen creativity temperature
        self.llm = ChatGroq(
            temperature=temperature,
            groq_api_key=os.getenv("GROQ_API_KEY"),  # Load secret key from environment
            model_name="llama-3.1-8b-instant"         # Fast Groq model for low-latency generation
        )

    # ------------------------------------------------------------
    # Generate a simple melody based on user input
    # ------------------------------------------------------------
    def generate_melody(self, user_input):
        """
        Generate a melody represented as space-separated note names.

        Parameters
        ----------
        user_input : str
            Natural language description of the musical idea.

        Returns
        -------
        str
            A sequence of note names (e.g., "C4 D4 E4 G4").
        """
        # Define the prompt template for melody generation
        prompt = ChatPromptTemplate.from_template(
            "Generate a melody based on this input: {input}. "
            "Represent it as space separated notes (e.g., C4 D4 E4)."
        )

        # Create a chain: prompt → LLM
        chain = prompt | self.llm

        # Execute the chain with the user input
        return chain.invoke({"input": user_input}).content.strip()

    # ------------------------------------------------------------
    # Generate harmony chords for an existing melody
    # ------------------------------------------------------------
    def generate_harmony(self, melody):
        """
        Produce harmony chords accompanying a melody.

        Parameters
        ----------
        melody : str
            Sequence of notes to be harmonised.

        Returns
        -------
        str
            Harmony chord progression (e.g., "C4-E4-G4 F4-A4-C5").
        """
        # Prompt instructing the model to create chord structures
        prompt = ChatPromptTemplate.from_template(
            "Create harmony chords for this melody: {melody}. "
            "Format: C4-E4-G4 F4-A4-C5"
        )

        chain = prompt | self.llm

        # Invoke with the melody input
        return chain.invoke({"melody": melody}).content.strip()

    # ------------------------------------------------------------
    # Suggest rhythm durations for a melody
    # ------------------------------------------------------------
    def generate_rythm(self, melody):
        """
        Suggest rhythm durations (in beats) for a melody.

        Parameters
        ----------
        melody : str
            Sequence of melodic note names.

        Returns
        -------
        str
            Rhythm pattern represented as beat durations
            (e.g., "1.0 0.5 0.5 2.0").
        """
        # Prompt to generate rhythmic values
        prompt = ChatPromptTemplate.from_template(
            "Suggest rhythm durations (in beats) for this melody: {melody}. "
            "Format: 1.0 0.5 0.5 2.0"
        )

        chain = prompt | self.llm

        return chain.invoke({"melody": melody}).content.strip()

    # ------------------------------------------------------------
    # Adapt melody, harmony, and rhythm to a musical style
    # ------------------------------------------------------------
    def adapt_style(self, style, melody, harmony, rhythm):
        """
        Adapt the given musical components to a chosen style.

        Parameters
        ----------
        style : str
            Name of the musical style (e.g., "jazz", "baroque", "lofi").
        melody : str
            Original melody.
        harmony : str
            Chord progression accompanying the melody.
        rhythm : str
            Rhythm durations.

        Returns
        -------
        str
            A single-string summary combining the adapted musical elements.
        """
        # Prompt to merge all elements into a style-specific transformation
        prompt = ChatPromptTemplate.from_template(
            "Adapt to {style} style:\n"
            "Melody: {melody}\n"
            "Harmony: {harmony}\n"
            "Rhythm: {rhythm}\n"
            "Output a single string summary."
        )

        chain = prompt | self.llm

        # Provide all inputs required for adaptation
        return chain.invoke({
            "style": style,
            "melody": melody,
            "harmony": harmony,
            "rhythm": rhythm
        }).content.strip()
