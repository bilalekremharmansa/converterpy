from converter.util.logger import LogManager
from converter.cli import Cli

logger = LogManager.get_logger()


def test_cli_usage():
    cli = Cli(logger)

    assert cli.usage() is not None
    assert cli.usage() != ''


def test_cli_parse():
    cli = Cli(logger)

    args = cli.parse('10 seconds to minutes'.split())
    assert args['source'] == 'seconds'
    assert args['value'] == '10'
    assert args['target'] == 'minutes'

    # ------

    args = cli.parse('10 sec to minn'.split())
    assert args['source'] == 'sec'
    assert args['value'] == '10'
    assert args['target'] == 'minn'


def test_cli_help():
    cli = Cli(logger)

    def _assert(statement):
        args = cli.parse(statement.split())
        assert args['help']

    # ------

    _assert('--help')
    _assert('-h')
    _assert('10 seconds to minutes -h')
    _assert('10 seconds to minutes --help')
    _assert('--help 10 seconds to minutes')
    _assert('-h 10 seconds to minutes')


def test_cli_verbose():
    cli = Cli(logger)

    def _assert(statement):
        args = cli.parse(statement.split())
        assert args['verbose']

    # ------

    _assert('10 seconds to minutes -v')
    _assert('10 seconds to minutes --verbose')
    _assert('--verbose 10 seconds to minutes')
    _assert('-v 10 seconds to minutes')


# multiple optional arg test
def test_cli_help_and_verbose():
    cli = Cli(logger)

    def _assert(statement):
        args = cli.parse(statement.split(' '))
        assert args['help']
        assert args['verbose']

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








