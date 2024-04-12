"""Define Encoder class and methods for encoding. """


class Encoder:
    def __init__(self, permutation_circles=list[str]):
        """The constructor takes a variable number of strings as argument.
        For example the string 'aeiou' means that
        a becomes e,
        e becomes i,
        ..
        o becomes u,
        u becomes a."""

    def encode(self, raw: str) -> str:
        """Encode the given string."""
        pass

    def decode(self, encoded: str) -> str:
        """Decode the given string."""
        pass
