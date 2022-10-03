#
# SPDX-License-Identifier: MIT
#
# Copyright (C) 2015-2022, AllWorldIT.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Docplates export built-in tests."""

import os
import pathlib
import shutil
import tempfile

import docplates

from ...base import BaseTest

__all__: list[str] = []


class TestDocplates(BaseTest):
    """Export built-in test."""

    def test_tex(self) -> None:  # pylint: disable=no-self-use
        """Export built-in test for .tex templates."""

        docp = docplates.Docplates(config={})

        mydir = pathlib.Path(os.path.dirname(__file__))
        helloworld_file = mydir.joinpath("helloworld.tex")

        with tempfile.TemporaryDirectory(prefix="docplates-test") as test_dir:
            # Work out destination paths
            test_dir_path = pathlib.Path(test_dir)
            test_file_src = test_dir_path.joinpath("helloworld.tex")
            test_file_dst = test_dir_path.joinpath("helloworld.pdf")

            # Copy source file
            shutil.copy(helloworld_file, test_file_src)
            # Generate PDF
            exports = docp.generate(input_file=test_file_src, output_file=test_file_dst, variables={})

            assert os.path.isfile(test_file_dst) is True, "PDF file not generated"
            assert exports == {"export_test": "export_value"}, "Export not found"

    def test_html(self) -> None:  # pylint: disable=no-self-use
        """Export built-in test for .html templates."""

        docp = docplates.Docplates(config={})

        mydir = pathlib.Path(os.path.dirname(__file__))
        helloworld_file = mydir.joinpath("helloworld.html")

        with tempfile.TemporaryDirectory(prefix="docplates-test") as test_dir:
            # Work out destination paths
            test_dir_path = pathlib.Path(test_dir)
            test_file_src = test_dir_path.joinpath("helloworld.html")
            test_file_dst = test_dir_path.joinpath("helloworld.pdf")

            # Copy source file
            shutil.copy(helloworld_file, test_file_src)
            # Generate PDF
            exports = docp.generate(input_file=test_file_src, output_file=test_file_dst, variables={})

            assert os.path.isfile(test_file_dst) is True, "PDF file not generated"
            assert exports == {"export_test": "export_value"}, "Export not found"
