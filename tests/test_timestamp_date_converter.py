from converterpy.converter.timestamp_date_converter import *


def test_init():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert converter is not None


def test_supported_conversions():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert UNIT_TIMESTAMP in converter.supported_conversions()
    assert UNIT_DATE in converter.supported_conversions()[UNIT_TIMESTAMP]

    assert UNIT_DATE in converter.supported_conversions()
    assert UNIT_TIMESTAMP in converter.supported_conversions()[UNIT_DATE]


def test_is_convertible():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert converter.is_convertible(UNIT_TIMESTAMP, UNIT_DATE)
    assert converter.is_convertible(UNIT_DATE, UNIT_TIMESTAMP)


def test_convert():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert converter.convert(UNIT_TIMESTAMP, 1610643651, UNIT_DATE) == '2021-01-14 17:00:51'
    assert converter.convert(UNIT_TIMESTAMP, 1545730073, UNIT_DATE) == '2018-12-25 09:27:53'
    assert converter.convert(UNIT_TIMESTAMP, 1386181800, UNIT_DATE) == '2013-12-04 18:30:00'

    # ----

    assert converter.convert(UNIT_TIMESTAMP, 0, UNIT_DATE) == '1970-01-01 00:00:00'
    assert converter.convert(UNIT_TIMESTAMP, 1, UNIT_DATE) == '1970-01-01 00:00:01'


def test_convert_timestamp_as_str():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert converter.convert(UNIT_TIMESTAMP, '1610643651', UNIT_DATE) == '2021-01-14 17:00:51'
    assert converter.convert(UNIT_TIMESTAMP, '1545730073', UNIT_DATE) == '2018-12-25 09:27:53'
    assert converter.convert(UNIT_TIMESTAMP, '1386181800', UNIT_DATE) == '2013-12-04 18:30:00'


def test_convert_date_to_ts():
    converter = TimestampDateConverter(timezone=datetime.timezone.utc)

    assert converter.convert(UNIT_DATE, '2021-01-14 17:00:51', UNIT_TIMESTAMP) == 1610643651
    # -----

    assert converter.convert(UNIT_DATE, '2018-12-25 09:27:53', UNIT_TIMESTAMP) == 1545730073
    assert converter.convert(UNIT_DATE, '2013-12-04 18:30:00', UNIT_TIMESTAMP) == 1386181800

    # -----

    assert converter.convert(UNIT_DATE, '2018-12-25', UNIT_TIMESTAMP) == 1545696000
    assert converter.convert(UNIT_DATE, '2013-12-04', UNIT_TIMESTAMP) == 1386115200

    # ------

    assert converter.convert(UNIT_DATE, '2021-01-14 00:00:00', UNIT_TIMESTAMP) == 1610582400
    assert converter.convert(UNIT_DATE, '2021-01-14', UNIT_TIMESTAMP) == 1610582400
