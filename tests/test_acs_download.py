#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `acs_download` package."""


import unittest
from click.testing import CliRunner

from acs_download import acs_download
from acs_download import cli


class TestAcs_download(unittest.TestCase):
    """Tests for `acs_download` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'acs_download.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert "--help  Download ACS PUMS entire data files from US Census Bureau's FTP server." in help_result.output
