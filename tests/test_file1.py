import pytest

from src.ArgumentParser import ArgumentParser
from src.flag_descriptions import (
    help_flag_description,
    ascii_flag_description,
    color_flag_description,
)


@pytest.fixture()
def parser():
    """
    Build a parser with deterministic flag functions for testing.
    This avoids randomness from art.text2art(font="random") and avoids ANSI codes.
    """
    p = ArgumentParser()

    def ascii_fn(argument: str, flag_argument: str = "") -> str:
        return f"ASCII({argument})"

    def color_fn(argument: str, flag_argument: str = "") -> str:
        # wrap so we can assert on exact output
        return f"<{flag_argument}>{argument}</{flag_argument}>"

    def help_fn() -> str:
        return help_flag_description

    p.add_flag(
        name=["-c", "--color"],
        fn=color_fn,
        description=color_flag_description,
        arguments=["red", "green", "blue"],
    )
    p.add_flag(
        name=["-a", "--ascii"],
        fn=ascii_fn,
        description=ascii_flag_description,
        arguments=[],
    )
    p.add_flag(
        name=["-h", "--help"],
        fn=help_fn,
        description=help_flag_description,
        arguments=[],
    )

    return p


def test_no_args_prints_help_and_exits(parser, capsys):
    with pytest.raises(SystemExit):
        parser.parse_args(["hello"])

    out = capsys.readouterr().out
    assert help_flag_description.strip() in out


def test_help_flag_prints_help_and_exits(parser, capsys):
    with pytest.raises(SystemExit):
        parser.parse_args(["hello", "-h"])

    out = capsys.readouterr().out
    assert help_flag_description.strip() in out


def test_unknown_flag_exits_with_message(parser, capsys):
    with pytest.raises(SystemExit):
        parser.parse_args(["hello", "--nope"])

    out = capsys.readouterr().out
    assert "No flag with name --nope found" in out


def test_color_flag_without_color_argument_exits_with_description(parser, capsys):
    # matches your parse_args branch that prints flags[0].description if only flags exist
    with pytest.raises(SystemExit):
        parser.parse_args(["hello", "-c"])

    out = capsys.readouterr().out
    assert color_flag_description.strip() in out


def test_ascii_only_flag_applies_to_argument(parser, capsys):
    # hello -a buna -> ASCII(buna)
    parser.parse_args(["hello", "-a", "buna"])
    out = capsys.readouterr().out
    assert "ASCII(buna)" in out


def test_color_then_ascii_results_in_colored_ascii(parser, capsys):
    # Expected: ascii first then color last => <red>ASCII(buna)</red>
    parser.parse_args(["hello", "-c", "red", "-a", "buna"])
    out = capsys.readouterr().out
    assert "<red>ASCII(buna)</red>" in out


def test_ascii_then_color_results_in_colored_ascii(parser, capsys):
    # Order shouldn't matter if you rearrange color to be last
    parser.parse_args(["hello", "-a", "buna", "-c", "red"])
    out = capsys.readouterr().out
    assert "<red>ASCII(buna)</red>" in out


def test_color_flag_not_applied_twice_when_both_aliases_present(parser, capsys):
    # If both -c and --color are used, you should not apply color twice.
    parser.parse_args(["hello", "-c", "--color", "red", "-a", "buna"])
    out = capsys.readouterr().out

    # should contain exactly one wrapped result
    assert "<red>ASCII(buna)</red>" in out
    assert out.count("<red>") == 1


def test_hello_a_red_should_keep_red_as_positional(parser, capsys):
    # Important behavior: red should NOT be consumed as a color argument if -c is not invoked
    # hello -a red -> ASCII(red)
    parser.parse_args(["hello", "-a", "red"])
    out = capsys.readouterr().out
    assert "ASCII(red)" in out
