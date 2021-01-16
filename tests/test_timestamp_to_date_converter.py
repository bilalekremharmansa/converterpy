from converterpy.converter.timestamp_date_converter import *


def test_init():
    converter = TimestampToDateConverter(timezone=datetime.timezone.utc)

    assert converter is not None


def test_supported_conversions():
    converter = TimestampToDateConverter(timezone=datetime.timezone.utc)

    assert UNIT_TIMESTAMP in converter.supported_conversions()
    assert UNIT_DATE in converter.supported_conversions()[UNIT_TIMESTAMP]


def test_is_convertible():
    converter = TimestampToDateConverter(timezone=datetime.timezone.utc)

    assert converter.is_convertible(UNIT_TIMESTAMP, UNIT_DATE)
    assert not converter.is_convertible(UNIT_DATE, UNIT_TIMESTAMP)


def test_convert():
    converter = TimestampToDateConverter(timezone=datetime.timezone.utc)

    assert converter.convert(UNIT_TIMESTAMP, 1610643651, UNIT_DATE) == '2021-01-14 17:00:51'
    assert converter.convert(UNIT_TIMESTAMP, 1545730073, UNIT_DATE) == '2018-12-25 09:27:53'
    assert converter.convert(UNIT_TIMESTAMP, 1386181800, UNIT_DATE) == '2013-12-04 18:30:00'

    # ----

    assert converter.convert(UNIT_TIMESTAMP, 0, UNIT_DATE) == '1970-01-01 00:00:00'
    assert converter.convert(UNIT_TIMESTAMP, 1, UNIT_DATE) == '1970-01-01 00:00:01'


def test_convert_timestamp_as_str():
    converter = TimestampToDateConverter(timezone=datetime.timezone.utc)

    assert converter.convert(UNIT_TIMESTAMP, '1610643651', UNIT_DATE) == '2021-01-14 17:00:51'
    assert converter.convert(UNIT_TIMESTAMP, '1545730073', UNIT_DATE) == '2018-12-25 09:27:53'
    assert converter.convert(UNIT_TIMESTAMP, '1386181800', UNIT_DATE) == '2013-12-04 18:30:00'
