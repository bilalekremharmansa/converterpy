from converterpy.util.assertion import assert_with_thrown

from converterpy.util.logger import LogManager
from converterpy.cli import Cli

logger = LogManager.get_logger()


def test_cli_convert():
    cli = Cli('10 seconds to minutes'.split())

    assert cli.action == 'convert'
    assert cli.source == 'seconds'
    assert cli.value == '10'
    assert cli.target == 'minutes'

    # ------

    cli = Cli('10 sec to minn'.split())
    assert cli.action == 'convert'
    assert cli.source == 'sec'
    assert cli.value == '10'
    assert cli.target == 'minn'


def test_cli_list():
    cli = Cli('list'.split())

    assert cli.action == 'list'
    assert cli.source is None

    # ------

    cli = Cli('list seconds'.split())
    assert cli.action == 'list'
    assert cli.source == 'seconds'


def test_cli_help():
    # docopt lib calls system.exit(), if --help is provided
    def _assert(statement):
        assert_with_thrown(lambda: Cli(statement.split()), SystemExit, lambda _: True)

    # ------

    _assert('--help')
    _assert('-h')
    _assert('10 seconds to minutes -h')
    _assert('10 seconds to minutes --help')
    _assert('--help 10 seconds to minutes')
    _assert('-h 10 seconds to minutes')


def test_cli_verbose():
    def _assert(statement):
        cli = Cli(statement.split())
        assert cli.verbose

    # ------

    _assert('10 seconds to minutes -v')
    _assert('10 seconds to minutes --verbose')
    _assert('--verbose 10 seconds to minutes')
    _assert('-v 10 seconds to minutes')


# multiple optional arg test
def test_cli_help_and_verbose():
    # docopt lib calls system.exit(), if --help is provided
    def _assert(statement):
        assert_with_thrown(lambda: Cli(statement.split()), SystemExit, lambda _: True)

    # ------

    _assert('--help --verbose')
    _assert('--help -v')
    _assert('-h --verbose')
    _assert('-h -v')

    # ------

    _assert('10 seconds to minutes -h -v')
    _assert('10 seconds to minutes --help -v')
    _assert('--help 10 seconds to minutes --verbose')
    _assert('-h 10 seconds to minutes --verbose')








